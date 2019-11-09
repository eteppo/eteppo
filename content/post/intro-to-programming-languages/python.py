# import gets object from known paths
# as renames object
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
# scikit-learn for data science
from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state
# goal: make random data, fit two different models, plot results
n = 100
# np has function arange; makes array from 0 to n
x = np.arange(n)
# check_random_state returns instance of class RandomState
rs = check_random_state(seed = 0)
# rs object has method randit to make random numbers
y = rs.randint(-50, 50, size = (n, )) + 50. * np.log1p(np.arange(n))
# get instance of IsotonicRegression
ir = IsotonicRegression()
# fit isotonic regression model to data
y_ = ir.fit_transform(x, y)
# get instance of LinearRegression
lr = LinearRegression()
# fit linear regression model to data
# x was array of length 100
# x[:, np.newaxis] is array for arrays of length 1
lr.fit(x[:, np.newaxis], y)
# segments is pairs of [x, y] points; prediction and data
# data structure is [[[x, y], [x, y_]], ...] 
segments = [[[i, y[i]], [i, y_[i]]] for i in range(n)]
# matplotlib has data structure called LineCollection
lc = LineCollection(segments, zorder = 0)
lc.set_array(np.ones(len(y)))
lc.set_linewidths(np.full(n, 0.5))
# matplotlib.pyplot allows building plot with various methods
plt.plot(x, y, 'r.', markersize=12)
plt.plot(x, y_, 'b.-', markersize=12)
plt.plot(x, lr.predict(x[:, np.newaxis]), 'b-')
plt.gca().add_collection(lc)
plt.legend(('Data', 'Isotonic Fit', 'Linear Fit'), loc='lower right')
plt.title('Isotonic regression')
plt.show()