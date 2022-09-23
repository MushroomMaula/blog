---
category: machine learning
date: 2022-08-22
---

# Linear Regression

If you ever had to fit a line to some data-points you quite possibly have come across _linear regression_ and _least squares_.
Most of the time _(linear) regression_ is introduced as follows:

Assume we have some target data $y \in \mathbb{R}^N$ and some observations $X \in \mathbb{R}^{N \times p}$ and our task is to 
fit a line $f(X_i) = w^T X_i + w_0$, which minimizes the error.

Now at this point the _mean squared error_ is often introduced:

$$ \text{MSE}(f) =  \frac{1}{N} \sum_{i=1}^N (y_i - f(X_i))^2$$

The question one should always ask: _Why exactly do we use this?_
If we ask ourselves which conditions the error function should satisfy, we will see that the (mean) squared error 
arises quite naturally.

- The error has to positive, i.e. $y_i - f(X_i) \ge 0$
- Small errors should have less influence than large errors
- Should be easy to optimize

All of these criterions are met for the squared error $(y_i - f(X_i))^2$. Squaring the error results in positive values and
values between $0$ and $1$ have less weight, while values greater than $1$ get further amplified. 
At the same time the least squares error has the solution $\hat{w} = (X^T X)^{-1} X^T y$.

Now even tough all of this sounds reasonable in my opinion there is a better way to introduce regression and least squares.


## Probabilistic introduction to Regression
As before we want to fit a line $f(X_i) = w^T X_i + w_0$ as good as possible to our target data $y$.
What this means, is we assume that the target values $y_i$ and the data have the following relationship:
$$ y_i = w^T X_i + w_0 + \epsilon_i $$

Here $\epsilon_i$ is a random error, that will always be present in real observations, which we assume to be drawn
from a normal distribution $\mathcal{N}(0, \sigma^2)$.

```{margin}
See this [stackexchange post](https://stats.stackexchange.com/questions/316936/linear-regression-proving-least-squares-model) for the
mathematical derivation.
```

Knowing this we can also express the conditional probability of $y$ in terms of a normal distribution:

$$ P(y_i | X_i) = \mathcal{N}(y_i | w^T X_i + w_0, \sigma^2) $$

Now we still want to find the best possible $w$ and $w_0$ for our data.
A simple way to fit a statistical model is to use _maximum likelihood estimation_ which involves maximizing the following likelihood function:
$$
L(w) = \prod_{i=1}^N \mathcal{N}(y_i | w^T X_i + w_0, \sigma^2)
$$

Taking the logarithm of the above expression, multiplying with $-1$ and plugging in the definition of the normal distribution, we can equally minimize:
$$
\begin{aligned}
   NLL(w) &= - \sum_{i=1}^N -\log \left[ \sqrt{\frac{1}{2 \pi \sigma^2}}  \exp \left( -\frac{1}{2\sigma^2}(y_i - w^T X_i - w_0) \right) \right]\\
      &= \frac{1}{2\sigma^2}\sum_{i = 1}^N (y_n - w^T X_i - w_0)^2 + \frac{N}{2}\log(2 \pi\sigma ^2)
\end{aligned}
$$

If you look closely the first term includes the _squared error_ we introduced earlier. At the same time the second term is a constant that
can be neglected, when minimizing.

```{margin}
The _residual sum of squares_ is defined as:
$$ RSS = \frac{1}{2} \sum_{i = 1}^N (y_n - f(X_i))^2 $$
```

The minimization problem at hand, $\mathop{\rm arg\,min}\limits_{w, w_0} \frac{1}{2\sigma^2}\sum_{i = 1}^N (y_n - w^T X_i - w_0)^2 $ is actually proportional to the 
_residual sum of squares_ and the _mean squared error_ introduced above.
Hence the solution to the maximum likelihood estimation is also:

$$ \hat{w} = (X^T X)^{-1} X^T y $$

To me this is quite a remarkable explanation of why we can use the squared error.


### One step further
```{margin}
Actually MLE is a special case of MAP with a uniform prior, as explained in this [post](https://agustinus.kristia.de/techblog/2017/01/01/mle-vs-map/) by Agustinus Kristiadi.
```
We can take the above one step further, if instead of a maximum likelihood estimation we use maximum a posteriori estimation.

$$
w_{MAP}, w_{0_{MAP}} = \mathop{\rm arg\,max}\limits_{w, w_0} \prod_{i=1}^N P(y_i | w^T X_i + w_0) \cdot P(\mathbf{w})
$$

Here $P(\mathbf{w})$ is the probability density of the prior we choose for the weights $w, w_0$ of our model.

Using this framework we can easily derive many regression models such as lasso and ridge regression as explained by the following table:

```{table} Summary of regression models for different likelihoods and priors. Likelihood refers to the distribution of $P(y_i | X_i)$ in this case.


| *Likelihood* | *Prior*  | *Name*            |
|:-------------|:---------|:------------------|
| Gaussian     | Uniform  | Least Squares     |
| Gaussian     | Gaussian | Ridge             |
| Gaussian     | Laplace  | Lasso             |
| Laplace      | Uniform  | Robust regression |
```


A in depth explanation of this topic can also be found in Chapter 11 of {cite:ps}`pml1Book`.

```{bibliography}
```