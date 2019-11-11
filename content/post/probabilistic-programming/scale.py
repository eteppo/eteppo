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