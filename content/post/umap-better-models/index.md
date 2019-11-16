+++
title = "The Fewer The Arbitrary Assumptions, The Better The Model – and the Uniform Manifold Approximation and Projection"
date = "2019-11-16"
+++

## The problem of bad assumptions

All models in data sciences in general are basically just a list of assumptions. The more accurate the assumptions are, the better the learned model will be. For example, images often contain a hierarchy of features with translational invariance – these assumptions point to representations called convolutional neural networks that were a big breakthrough in computer vision.

Now, the problem is that this is not how data science is often done. Instead, analysts are not sure what assumptions to make and use a canned algorithm that happens to be the standard in your field for the kind of data that you roughly have – or they select the algorithm that has been empirically superior among some benchmarks.

I wrote <a href="https://eteppo.com/post/probabilistic-programming/" target="_blank">a little piece</a> on probabilistic programming as a framework that makes architectures and the handling of uncertainty much less arbitrary but I want to take things further in this post. Even those fairly general algorithms with a cool name – like _ConvNets_ for images – should be developed based on non-arbitrary, general mathematical assumptions about the data generation.

## What is the structure of datasets like?

Common assumptions about the structure of datasets include linearity, sparsity, independence, high-dimensional crowding (curse of dimensionality), Euclidean space, particular kinds of densities, outliers and noise, local or global patterns, and so on.

Mostly these try to make things simpler, easier, faster, more interpretable, and many datasets do follow these assumptions. For example, simple equations have been shown to be just as good at predicting many health-related things as much more flexible deep networks. Also, by combining lots of different algorithms you get many views on the data space – it's no surprise that large model ensembles are usually the best when it comes to prediction accuracy.

However, often things feel too arbitrary so I really enjoyed to learn about UMAP. UMAP is a great example of another kind of method so let's go through how it roughly works. 

The rest of the post is based on <a href="https://umap-learn.readthedocs.io/en/latest/">the UMAP Python documentation</a>.

## How about locally connected manifolds with locally constant Riemannian metrics?

UMAP basically assumes that the data points are distributed uniformly on a locally connected Riemannian manifold with a locally constant (Riemannian) metric tensor. This kind of smooth, fuzzy surface is extremely flexible yet provides reasonable and informative global and local constraints from a mathematically natural (in contrast to arbitrary) basis. 

It feels a bit like the hierarchical features assumption in deep neural networks although there is a lot less mathematical theory, theorems, and proofs in the background there. Topological methods generalize many mathematical structures. Clusters are 0-dimensional holes, lines are 1-simpleces, triangles are 2-simpleces, graphs are simplicial complexes with only 0- and 1-simpleces, and Euclidean space is just a particular topological space. 

UMAP is based on a particular kind of simplicial complex (Vietoris-Rips) that cover the assumed surface. This requires approximating an open cover of the surface and UMAP does this by basically taking a binary-fuzzy-hybrid area around each data point.

The radius of the point area is not simply defined as a hyperparameter. Instead, UMAP assumes that the points are distributed uniformly, warps the space so that this assumption becomes true, and basically sets all of the areas to have a constant radius in the new space. Each point is equally distant from its neighbors given that each point has its own measure of distance. All points are connected to at least one neighbor in a binary way (local connectivity) and others beyond that in a fuzzy way.

If we switched back to the original space and looked what the distance measure was, it would happen to be the distance to the kth nearest neighbor. You select the hyperparameter _k_ according to how much of the points in the neighborhood you want to include to estimating the local Riemannian metric tensor (distance measure) of the given point. Furthermore, this cover just happens to resolve the crowding problem because the fuzzy outer area measures relative instead of absolute distances.

Finally, UMAP resolves disagreeing local metrics by taking the union of the fuzzy simplicial sets which pops out an intuitive probabilistic summary measure.

Most importantly, all of the above is done because a theorem, some algebraic topology functors, and fuzzy simplicial set math say that the fuzzy simplicial complexes cover the Riemannian manifold when you do these things. You can really feel the lack of arbitrary decisions.

## Good models naturally pop out from strong general theories in physics too

This phenomenon that strong generalized theories have previous models as natural special cases is a really good sign. As a rule of thumb, when you start hacking arbitrary summary functions and thresholds in your methods, step back and try to think about the assumptions more generally. You might find a way to let the math do that work and create a model that encodes much more accurate information about your data.

Something similar to this happens in physics. The Einstein's theory of gravity, general relativity, uses a similar pseudo-Riemannian geometry that UMAP is based on. It describes how our physical space-time is curved due to mass and energy insanely accurately. Einstein took relatively simple assumptions about the universe – like that all observers measure the speed of light to be the same – and everything else fell into place after that. When you move at slow speeds, general relativity pops out the Newtonian theory of gravity as a special case. 

Now physicists are working on even more general theories of everything and it is a very good sign that something like general relativity and quantum mechanics pop out from the more general theory. It's also a really good sign that the theory is not based on arbitrary assumptions but rather almost seems to write itself. Many physicists seem to think string theory is a strong contender precisely because it has been developed like that. On the other hand, string theorists had to assume a large number of spatial dimensions because the theory doesn't work without them which seems to decrease its ultimate plausibility.