+++
title = "Artificial Intelligence: A Simple Overview"
date = "2019-07-27"
+++

Artificial intelligence refers to the intelligence – or the problem solving ability – of machines. You can think of AI agents as systems that have the following parts.

{{<figure src="ai-agent.png">}}

They sense, predict, act, and learn in their environments in order to maximize some kind of performance measure.

There's an infinite space of possible methods to use. Here's just a few them across fields of AI. (Open in a new tab or save as a file to explore.)

{{<figure src="ai-algorithms.png">}}

More importantly, all AI problems have just a few core elements.

First, you need to define some _task_ or problem to solve. It's best to think of all possible tasks as some sort of _prediction_. Below, you can see lots of special cases of prediction tasks that are thrown around.

As an AI developer you also need to think about how to come up with good candidate problems and how to prioritize them. That's of course prediction too but in this case on a higher meta level.

{{<figure src="1-problem-space.png">}}

Let's say the sensors, actuators, and resources are ready. The sensors produce data.

Data is just any raw information from the sensors. Usually you need to clean and wrangle with it a lot to use it to train an agent. This preprocessing basically happens at the sensor level.

It's easy to think of data as points in space. Each point represents one observational unit (like a person) and the position of the point represents values of a set of variables (like pain, weight, temperature). You can think of images as points in a 1000-dimensional space or however many pixels the image contains. And so on for any kind of sensory input.

{{<figure src="dataset-visual-2d.png">}}

Now you can think of predicting as assigning some predicted values to each position in the _data space_. Very intuitive.

{{<figure src="hyperplanes.png">}}

Let's move on to the actual agent function.

First, you need to set up an agent program that represents some kind of assumptions about the task and the agent. You don't want to assume too much so that the agent has lots of room to get better.

The point of AI is that you don't know how to write a program that solves some problem so you write an agent that learns and reasons by itself.

This is called the _representation_. Essentially, you write a skeleton with a bunch of tuning knobs. Tuning knobs can be anything about the program that you don't fix. Anything that the agent can change about the program while learning. (Open in a new tab or save as a file to explore.)

{{<figure src="2-models.png">}}

Next, the agent needs some measure of how good any particular candidate program is. This is called the _evaluation_ or loss function. You could use almost anything – usually it's just some simple measure of prediction accuracy.

{{<figure src = "3-evaluation-criticism.png">}}

Finally, the agent needs to have some kind of method of selecting new candidate programs, testing them, and refining the program. This is called _optimization_ or just _learning_.

{{<figure src = "4-inference-learning.png">}}

It's good to know about the four basic kinds of supervision.

_Supervised_ learning is the most straight-forward situation where the program just gets both inputs and outputs and tries to learn how to do similar predictions for new inputs.

{{<figure src = "supervised-data.png">}}

Any proportion of the correct outputs or predictions can be also unknown to the agent. This is _semi-supervised_ learning.

{{<figure src = "semi-supervised-data.png">}}

If all of the correct outputs are unknown to the agent, we call it _unsupervised_ learning. A good method could basically still learn the same patterns in the data space.

{{<figure src = "unsupervised-data.png">}}

Finally, instead of giving correct observations, you could just give any kind of feedback. With a good _reinforcement_ learning method, the agent can explore the environment, collect observations on its own and learn to predict so that the feedback gets better and better.

{{<figure src = "reinforcement-data.png">}}

In summary, it's very useful to keep in mind the following core elements of AI:

* Problem space – all possible tasks and problems are just different kind of prediction
* Agent architecture – environment, sensors, data, agent function, performance measure, resources, actuators
* Data space – all possible observations and actions
* Representation – what is assumed and fixed about the agent program
* The evaluation function – which candidate programs are better than others
* Optimization – how to take data and feedback and tweak the represention to get better evaluations