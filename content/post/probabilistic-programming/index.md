+++
title = "All Models are Special Cases of Probabilistic Programs"
date = "2019-11-11"
+++

If you've had any exposure to data sciences like statistics, machine learning, or some field of informatics, you've probably experienced how overwhelming the amount of algorithms can be. Fortunately, this complexity is just an illusion. In this post I'll try to show you with examples how encoding assumptions with basic computational building blocks – instead of picking from thousands of algorithms – can make data analysis way simpler and more intuitive, transparent, and effective.

All of the examples are modified from tutorials or examples of the corresponding software packages.

## Simple linear regression

Let's assume we have two variables – input and output. We want to figure out the unknown program that takes the input and spits out the output. We assume that the pattern is a straight line and that the prediction error follows a Gaussian function with a standard deviation of 1. We want to find the most likely program of this kind given our data. Any search method that can do the job is fine. 

This corresponds to the classical ordinary least squares regression model. However, we want to use general computational building blocks only.

First, the straight line can be represented as what is often called a _layer_ of computation. Our layer has a weight for the input variable and a so-called bias which is just a number that we add to the multiplication. This is often called a _dense_ layer since all input variables are connected to all output variables. Layers are a wonderful mid-level abstraction to stitch together very complex and deep learnable programs.

Second, the prediction error is another layer that just adds a random number to the output from the first layer. This is represented by a distribution component. Distributions are the key components of probabilistic programs.

Third, our evaluation function is the negative log-likelihood and we use the Adam optimizer to find the model that minimizes it. Unlike models, optimizers can be treated as black boxes and canned products without many problems.

Let's define it using Python, Keras, Tensorflow, and Tensorflow Probability.

```python
# software
import tensorflow.keras.models as tfkm
import tensorflow.keras.layers as tfkl
import tensorflow.keras.optimizers as tfko
import tensorflow_probability as tfp
tfpl = tfp.layers
tfpd = tfp.distributions
# initialize model as a sequence of two layers
model = tfkm.Sequential([
	# bias + weight * input using layer component
	# no activation or regularizers, default initializers
  tfkl.Dense(units = 1, use_bias = True),
  # Dense's output is the mean of the Gaussian distribution
  tfpl.DistributionLambda(lambda mean: tfpd.Normal(loc = mean, scale = 1))
])
# negative log likelihood measures how good the program is
def evaluate(truth, prediction):
  return -prediction.log_prob(truth)
# initialize a version of Adam who is good at finding the best program
optimizer = tfko.Adam(
	learning_rate = 0.01, 
	beta_1 = 0.9, 
	beta_2 = 0.999, 
	amsgrad = False
)
# run optimization
model.compile(optimizer = optimizer, loss = evaluate)
model.fit(input_train, output_train, epochs = 1000, verbose = False)
# model object contains all necessary result information
```

## A noisy scale

Let's try modelling an arbitrary system – a scale that is so noisy that it needs to be supplied with a good old human guess to get reasonable results. We can represent the guess and the measurement with distributions. For the sake of demonstration, let's also say that our guess (input) is 8.5 kg and the scale's measurement is 9.5 kg – what's the real weight of the object?

Let's use Python, PyTorch, and Pyro to model this system and answer the question.

```python 
# software
from torch import tensor, abs
from pyro import sample, param, condition, clear_param_store
from pyro.infer import Trace_ELBO, SVI
from pyro.optim import SGD
from pyro.distributions import Normal
# representation
def scale(guess):
    # real weight is guess plus some error
    guess_error = 1.0
    weight = sample("weight", Normal(guess, guess_error))
    # scale measures real weight with some error
    measurement_error = 1.0
    measurement = sample("measurement", Normal(weight, measurement_error))
    return measurement
# observe measurement and condition the scale on it
guess = 8.5
measurement = 9.5
conditioned_scale = condition(scale, data = {"measurement": measurement})
# optimization with stochastic variational inference
# requires an approximate posterior distribution
def scale_guide(guess):
    mean = param("mean", tensor(guess))
    sd = param("sd", tensor(1.0))
    measurement = sample("weight", Normal(mean, abs(sd)))
    return measurement
# reset parameter data
clear_param_store()
# compile optimization routine
svi = SVI(
    model = conditioned_scale,
    guide = scale_guide,
    # optimizer = stochastic gradient descent
    optim = SGD({"lr": 0.001, "momentum":0.1}),
    # evaluation measure = evidence lower bound / KL divergence
    loss = Trace_ELBO()
)
# run optimization
mean, sd = [], []
num_steps = 2500
for step in range(num_steps):
    svi.step(guess)
    mean.append(param("mean").item())
    sd.append(param("sd").item())
# print results from parameter data
print('mean =', param("mean").item())
print('sd =', param("sd").item())
```

The real weight is about 9.0 +/- 0.7SD.

## Factor analysis

Let's say you have a theory that the five variables that you have in your dataset could be actually thought to be a manifestation of two latent variables. For example, dozen or so symptoms could be a manifestation of concepts called _depression_ and _anxiety disorder_. We can model this simply with a multivariate distribution over the observed variables and latent variables, weights, and some error in the inputs.

This roughly corresponds to the so-called _factor analysis_ that is one of the popular methods to represent many variables with a smaller set of variables (dimension reduction).

This time we use R and greta but the basic components are pretty much the same.

```r
# software
library(greta)
# two unobservable variables (factors) and weights and errors
factors <- normal(mean = 0, sd = 1, dim = c(2, 100))
weights <- normal(mean = 0, sd = 1, dim = c(5, 2))
errors <- zeros(5, 5)
diag(errors) <- inverse_gamma(alpha = 1, beta = 1, dim = 5)
# parametrize a likelihood distribution over output data with p = 5 and n = 100
# %*% is a short-hand for matrix multiplication, t for transpose
distribution(output) <- multivariate_normal(t(weights %*% factors), errors)
# compile model with tracked variables 
model <- model(factors, weights)
# run inference with Hamiltonian Markov Chain Monte Carlo
posteriors <- mcmc(model, sampler = hmc())
# if diagnostics raise concerns, something's wrong in data, model, or inference
```

## Clinical trials

How about modelling clinical trials? Again, we could model arbitrarily complex trial designs. In the probabilistic programming world we are not restricted to simple canned statistical tools, like a particular frequentist statistical test. Instead, we can give treatment effectiveness a plausible prior, model the two alternatives where the treatment is effective and ineffective, infer the model given some data, and query what the posterior distributions over some relevant parameters look like. 

Let's use C#, .NET, and Microsoft.ML.Probabilistic for a change.

```cs
using Microsoft.ML;
using Microsoft.ML.Probabilistic;
using Microsoft.ML.Probabilistic.Distributions;
using Microsoft.ML.Probabilistic.Models;

namespace ClinicalTrial {

  class Program {
    static void Main(string[] args) {
      // Randomize patients equally to treatment or control
      // Measure their outcome (true for good or false for bad)
      VariableArray<bool> controlGroup = Variable.Observed(
        new bool[] { false, false, false, false, false, true, false, true, true, false }
      );
      VariableArray<bool> treatmentGroup = Variable.Observed(
        new bool[] { true, false, true, true, true, false, true, true, true, true }
      );
      Range i = controlGroup.Range; 
      Range j = treatmentGroup.Range;
      // Assume 25 % chance that treatment is effective before data
      Variable<bool> isEffective = Variable.Bernoulli(0.25);

      Variable<double> probIfTreated, probIfControl;
      // If treatment is effective, groups have different chances of good outcome
      // Patients within the same group have the same chance of good outcome
      using (Variable.If(isEffective)) {
        probIfControl = Variable.Beta(1, 1);
        probIfTreated = Variable.Beta(1, 1);
        controlGroup[i] = Variable.Bernoulli(probIfControl).ForEach(i);  
        treatmentGroup[j] = Variable.Bernoulli(probIfTreated).ForEach(j);  
      }
      // If treatment is not effective, everyone has the same chance of good outcome
      using (Variable.IfNot(isEffective)) {
        Variable<double> probAll = Variable.Beta(1, 1);
        controlGroup[i] = Variable.Bernoulli(probAll).ForEach(i);  
        treatmentGroup[j] = Variable.Bernoulli(probAll).ForEach(j);  
      }
      // Initialize inference engine
      InferenceEngine ie = new InferenceEngine();
      // Infer parameters of interest
      string pEffect = ie.Infer(isEffective).ToString();
      string pTreated = ie.Infer(probIfTreated).ToString();
      string pControl = ie.Infer(probIfControl).ToString();
      // Print out results 
      System.Console.WriteLine("P(effect | data) = " + pEffect);
      System.Console.WriteLine("P(good | treatment) = " + pTreated);  
      System.Console.WriteLine("P(good | control) = " + pControl);
    }
  }
}
```

If you assign 25 % of effectiveness before the trial, you should assign 64 % after this small trial according to probability theory. Here's the printed output:

```
P(effect | data) = Bernoulli(0.6428)
P(good | treatment) = Beta(9,3)[mean=0.75]
P(good | control) = Beta(4,8)[mean=0.3333]
```

## Hidden Markov Model

Let's imagine that we have measured whether children have an allergy five times during their childhood. The measurement is not perfect but has some error. How would you model this? Basically, we have five latent variables with connections to the next latent variable by time and to the five observed variables for the same time point. 

This model corresponds to a so-called <a href="https://en.wikipedia.org/wiki/Hidden_Markov_model" target="_blank">Hidden Markov Model</a>. Let's code something like it – this time using another probabilistic programming language – the WebPPL implemented in JavaScript.

```javascript
// data
const data = {obs: [true, false, false, false]};

// If the hidden state is true, next hidden state is 70 % true
let transition = function(state) {
  return state ? flip(0.7) : flip(0.3);
}
// If the hidden state is true, the observed variable is 90 % true
let observation = function(state) {
  return state ? flip(0.9) : flip(0.1);
}

let simulate = function(n_trans) {
  // recurse until n_trans is 1 and start from hidden state true
  // then "previous" will be assigned to be the previously returned dictionary
  let previous = (n_trans == 1) ? {states: [true], obs: []} : simulate(n_trans - 1);
  // transition to new hidden state
  let newState = transition(previous.states[previous.states.length - 1]);
  // measure value of the observeable variable related to the state
  let newObs = observation(newState);
  // merge previous and new values
  return {
    states: previous.states.concat([newState]),
    obs: previous.obs.concat([newObs])
  }
}

let model = function() {
  // run simulations similar to data
  let results = simulate(data.obs.length);
  // soft-condition inference on observed data
  factor(_.isEqual(results.obs, data.obs) ? 0 : -Infinity);
  return results.states
}
// run inference
let distribution = Infer({method: "enumerate"}, model);
// print results
console.log(distribution);
// hidden states were [true, false, false, false] with 75 % probability
// run with webppl command line tool (webppl.org)
```

This is the probability distribution that I got over the hidden states:

```
Marginal:
    [true,true,false,false,false] : 0.7534562073121731
    [true,false,false,false,false] : 0.08371735636801933
    [true,true,true,false,false] : 0.08371735636801933
    [true,true,false,false,true] : 0.035878867014865375
    [true,true,false,true,false] : 0.015376657292085169
    [true,true,true,true,false] : 0.009301928485335481
    [true,true,true,false,true] : 0.003986540779429489
    [true,true,false,true,true] : 0.003986540779429489
    [true,false,false,false,true] : 0.003986540779429489
    [true,true,true,true,true] : 0.002411611088790676
    [true,false,true,false,false] : 0.001708517476898351
    [true,false,false,true,false] : 0.001708517476898351
    [true,false,false,true,true] : 0.0004429489754921651
    [true,false,true,true,false] : 0.0001898352752109278
    [true,false,true,false,true] : 0.00008135797509039756
    [true,false,true,true,true] : 0.000049216552832462674
```