+++
title = "Less Arbitrary Assumptions Make Better Models"
date = "2019-11-16"
+++

## The problem of bad assumptions

All models in data sciences are basically lists of assumptions. The more accurate the assumptions are, the better the learned model will be. For example, images often contain a hierarchy of features with translational invariance – these assumptions point to representations called convolutional neural networks that were a big breakthrough in computer vision.

<a href="https://www.asimovinstitute.org/neural-network-zoo/"><img src="https://www.asimovinstitute.org/wp-content/uploads/2019/04/NeuralNetworkZoo20042019-1400x2380.png"></a>

Now, the problem is that this is not how data science is often done. Instead, analysts are not sure what assumptions to make and use a canned algorithm that happens to be the standard in your field for the kind of data that you roughly have – or they select the algorithm that has been empirically superior among some benchmarks.

I wrote a <a href="https://eteppo.com/post/probabilistic-programming/" target="_blank"> little piece</a> on probabilistic programming as a framework that makes architectures, handling of uncertainty, and other things much less arbitrary but I want to take things further in this post. All algorithms with cool names – like _ConvNets_ for images – should be developed based on good, non-arbitrary, general mathematical assumptions about the data.

## What is the structure of datasets like?

Unsupervised learning is all about finding the structure of datasets without help from other data. Common assumptions about the structure of datasets include linearity, sparsity, independence, high-dimensional crowding (curse of dimensionality), Euclidean space, particular kinds of densities, outliers and noise, local or global patterns, and so on.

Mostly this tries to make things easier and many datasets do follow these assumptions. For example, simple equations have been shown to be basically just as good at predicting many health-related things as much more flexible deep networks. Also, by combining lots of different algorithms you get many views on the data space – it's no surprise that large model ensembles are usually the best when it comes to prediction accuracy.

However, often the assumptions are just taken for granted with no relation to the underlying problem or mathematical theory. This feels so arbitrary that I really enjoyed learning about the Uniform Manifold Approximation and Projection algorithm. UMAP is a great example of another kind of method that is based on solid mathematical theory and better general assumptions about the structure of data. 

So let's go through how it roughly works. The rest of the post is based on the UMAP Python <a href="https://umap-learn.readthedocs.io/en/latest/" target="_blank">documentation</a>.

<a href="https://www.quora.com/What-is-a-manifold-in-laymans-terms" target="_blank"><img src="https://qph.fs.quoracdn.net/main-qimg-ab41f71f2d4dfff25bdba08dcc9fde81"></a>

## How about locally connected manifolds with locally constant Riemannian metrics?

UMAP basically assumes that the data points are distributed uniformly on a locally connected Riemannian manifold with a locally constant (Riemannian) metric tensor. This kind of smooth surface is extremely flexible yet provides a reasonable and informative global and local assumptions about the data from a mathematically natural – in contrast to arbitrary – basis. 

UMAP is heavily based on topology. Topological methods generalize many mathematical structures. Clusters are 0-dimensional holes, lines are 1-simpleces, triangles are 2-simpleces, graphs are simplicial complexes of 0- and 1-simpleces, and the standard Euclidean space is just a particular topological space.

First, to deal with a Riemannian topological space with data, UMAP uses a particular kind of <a href="https://en.wikipedia.org/wiki/Vietoris%E2%80%93Rips_complex" target="_blank">simplicial complex</a> that covers the assumed surface where the data is. Getting that requires approximating an open cover of the surface and UMAP does this by basically taking a binary-fuzzy-hybrid area around each data point.

<a href="https://umap-learn.readthedocs.io/en/latest" target="_blank"><img src="https://umap-learn.readthedocs.io/en/latest/_images/how_umap_works_umap_open_cover.png"></a>

The important point here is that the point area is not simply defined as a hyperparameter. Instead, UMAP assumes that the points are distributed uniformly, warps the _space_ so that this assumption becomes true, and basically sets all of the areas to have a constant radius in the new space. Each point is equally distant from its neighbors given that each point has its own measure of distance. The math tells that you need to assume local connectivity so all points are connected to at least one neighbor in a binary way and others beyond that in a fuzzy way.

If we switched back to the original space and looked what the distance measure was, it would happen to be the distance to the kth nearest neighbor. You select the hyperparameter _k_ according to how much of the points in the neighborhood you want to include to estimating the local Riemannian metric tensor (distance measure) of the given point. It a fairly intuitive hyperparameter to control the signal-noise-ratio and level of detail needed. Furthermore, this cover just happens to resolve the crowding problem because the fuzzy outer area measures relative instead of absolute distances.

Finally, UMAP resolves disagreeing local metrics by taking the union of the fuzzy simplicial sets which pops out an intuitive probabilistic summary measure.

<a href="https://en.wikipedia.org/wiki/Curvature_of_Riemannian_manifolds"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Gaussian_curvature.svg/800px-Gaussian_curvature.svg.png"></a>

Most importantly, all of the above is done because a theorem, some algebraic topology functors, fuzzy simplicial set math, and so on say that the fuzzy simplicial complexes only covers the Riemannian manifold when you do these things.

If my explanation of the method was somewhat sober, it should feel much less arbitrary than most other methods.

## Good models naturally pop out from strong general theories

As a rule of thumb, when you start hacking arbitrary summary functions and thresholds in your methods, step back and try to think about the assumptions and the language that they are represented in (math) more generally. You might find a way to let the math do the work and create a model that encodes much more accurate information about your data.

A close analogy in physics is worth a mention here.

The Einstein's theory of gravity, general relativity, uses a similar pseudo-Riemannian geometry that UMAP is based on. It describes how our physical space-time is curved due to mass and energy insanely accurately. Einstein took relatively simple assumptions about the universe – like that all observers measure the speed of light to be the same – and everything else fell into place after that. When you move at slow speeds, general relativity pops out the Newtonian theory of gravity as a special case. 

Now physicists are working on even more general theories of everything and it is a very good sign that something like general relativity and quantum mechanics pop out from the more general theory. It's also a really good sign that the theory is not based on arbitrary assumptions but rather almost seems to write itself. Many physicists seem to think string theory is a strong contender precisely because it has been developed like that. On the other hand, string theorists had to assume a large number of spatial dimensions because the theory doesn't work without them which seems to decrease its ultimate plausibility.