from numpy import sin, newaxis, linspace, float32, squeeze
from numpy.random import seed, rand, randn
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Dense
from tensorflow.keras.backend import variable
import tensorflow_probability as tfp
tfpl = tfp.layers
tfpd = tfp.distributions

tensorboard_callback = TensorBoard(log_dir="./regression-1-logs", histogram_freq=1)

def load_dataset(w0, b0, x_range, n=150, n_tst=150):
  seed(43)
  def s(x):
    g = (x - x_range[0]) / (x_range[1] - x_range[0])
    return 3 * (0.25 + g**2.)
  x = (x_range[1] - x_range[0]) * rand(n) + x_range[0]
  eps = randn(n) * s(x)
  y = (w0 * x * (1. + sin(x)) + b0) + eps
  x = x[..., newaxis]
  x_tst = linspace(*x_range, num=n_tst).astype(float32)
  x_tst = x_tst[..., newaxis]
  return y, x, x_tst

output_train, input_train, input_test = load_dataset(0.125, 5.0, [-20, 60])

def evaluate(truth, prediction):
  return -prediction.log_prob(truth)

optimizer = Adam(learning_rate = 0.01, beta_1=0.9, beta_2=0.999, amsgrad=False)

model = Sequential([
  Dense(1),
  tfpl.DistributionLambda(lambda mean: tfpd.Normal(loc=mean, scale=1))
])

model.compile(
  optimizer = optimizer, 
  loss = evaluate
)
model.fit(input_train, output_train, 
  epochs = 1000, verbose = False, 
  callbacks = [tensorboard_callback]
)

for weight in model.weights:
  print(squeeze(weight.numpy()))