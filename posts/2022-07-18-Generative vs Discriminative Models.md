---
category: machine learning
date: 2022-07-18
---
# Generative vs Discriminative Models
In this post we are going to explore the differences between *generative* and *discriminative* models.
In many machine learning tasks we assume that the output $y$ can be generate from some function $f(x)$, which is dependant on the input. We assume that we can model this function $f$ using the conditional probability $P(y|x)$.

Now there are two fundamentally different approaches to estimating $P(y|x)$:

## Generative models
A generative model calculates the *joint* probability density $P(x, y)$, which can also be used to generate new data pairs $(x, y)$ or to discriminate using *Bayes' rule*:
$$ P(y|x) = \frac{P(x|y) \cdot P(y)}{P(x)} = \frac{P(x, y)}{P(x)} $$

Examples for generative models include: [linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis) and [naive Bayes' classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)

## Discriminative models
A discriminative model on the other hand only "learns" the posterior probability $P(y|x)$ and is not able to generate new data.

Examples for discriminative models are: [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression), [support vector machines](https://en.wikipedia.org/wiki/Support-vector_machine) and [decision trees](https://en.wikipedia.org/wiki/Logistic_regression)


More generally we can say that a generative model learns the distribution of the classes, so that we can generate new instances, while a discriminative model learns the decision boundary between the classes.


### References
- <https://en.wikipedia.org/wiki/Generative_model>
- <https://en.wikipedia.org/wiki/Discriminative_model>
- <https://stackoverflow.com/questions/879432/what-is-the-difference-between-a-generative-and-a-discriminative-algorithm>
- <https://stats.stackexchange.com/questions/12421/generative-vs-discriminative/>
