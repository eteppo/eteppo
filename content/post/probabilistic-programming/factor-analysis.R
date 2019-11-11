

generate.data <- function(n = 100, p = 5, q = 2, psi = diag(rgamma(p, 1, 1)))
{
  W  <- matrix(rnorm(p * q, 1), p, q)
  Z  <- matrix(rnorm(q * n, 2), q, n)
  WZ <- W %*% Z
  
  X  <- matrix(0, n, p)
  for (i in seq_len(n)) {
    X[i, ] <- MASS::mvrnorm(1, WZ[, i], psi)
  }
  
  list(X = X, W = W, Z = Z, psi = psi)
}

n <- 100
p <- 5
q <- 2
data <- generate.data(n = n, p = p, q = q)
X <- data$X

W <- normal(0, 1, dim = c(p, q))
Z <- normal(0, 1, dim = c(q, n))
psi <- zeros(p, p)
diag(psi) <- inverse_gamma(1, 1, dim = p)

distribution(X) <- multivariate_normal(t(W %*% Z), psi)

draws <- mcmc(model(W, Z), one_by_one = TRUE)

bayesplot::mcmc_trace(draws)
