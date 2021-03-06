# Bayes factors

Bayes factors are a common alternative to information criteria. And a subject that generally acts as a dividing line between Bayesians: We have those who use Bayes factors and those who dislike them. I mean, I bet there are people in the middle too, but more often than not this is a polarizing topic.

To understand Bayes factors let us begin by writing Bayes theorem in a way that explicitly shows that our inferences are always model dependent.

$$p(\theta \mid y, M_k) = {\frac {p(y \mid \theta, M_k)p(\theta \mid M_k)}{p(y \mid M_k)}}$$

Where $y$ represents the data and $M$ the model:

The term in the denominator is known as marginal likelihood (or evidence). When doing inference we do not need to compute this normalizing constant, so in practice we often compute the posterior up to a constant factor. However, for model comparison and model averaging the marginal likelihood becomes a relevant quantity. If our main objective is to choose only one model, the best one, from a set of $k$ models we can just choose the one with the largest $p(y \mid M_k)$. As a general rule $p(y \mid M_k)$ are tiny numbers and do not tell us too much on their own; like with information criteria, what matters are the relative values. So in practice people often compute the ratio of two marginal likelihoods, and this is called a Bayes factor:


$$BF = \frac{p(y \mid M_0)}{p(y \mid M_1)}$$

Then when BF > 1, model 0 explains data better than model 1.

Some authors have proposed tables with ranges to discretize and ease BF interpretation. The following table indicates the strength of the evidence favoring model 0 against model 1:

* 1-3: anecdotal
* 3-10: moderate
* 10-30: strong
* 30-100: very strong
* \> 100: extreme

Remember, these rules are just conventions, simple guides at best. But results should always be put into context and should be accompanied with enough detail so others could potentially check if they agree with our conclusions. The strength of the evidence necessary to make a claim is not the same in particle physics, a court, or to evacuate a town and prevent hundreds of deaths.

Using $p(y \mid M_k)$ to compare model is totally fine if all models are assumed to have the same prior probability[<sup>1</sup>](#fn1). Otherwise, we have to compute the *posterior odds*:

$$\underbrace{\frac{p(M_0 \mid y)}{p(M_1 \mid y)}}_\text{posterior odds} = \underbrace{\frac{p(y \mid M_0)}{p(y \mid M_1)}}_\text{Bayes factors} \, \underbrace{\frac{p(\ M_0 \ )}{p(\ M_1 \ )}}_\text{prior odds}$$

<span id="fn1"> <sup>1</sup> Notice that we are talking about the prior probability we assign to models and not about the priors we assign to parameters for each model</span>


## All that glitter is not gold

Now we will briefly discuss some key facts about the marginal likelihood. By carefully inspecting the definition of marginal likelihood we can understand their properties and consequences for their practical use:

$$p(y \mid M_k) = \int_{\theta_k} p(y \mid \theta_k, M_k) p(\theta_k, M_k) d\theta_k$$


* **The good: Models with more parameters have a larger penalization than models with fewer parameters**. Bayes factors has a built-in Occam Razor! The intuitive reason is that the larger the number of parameters the more *spread-out* the prior will be with respect to the likelihood. Or in other words a more *spread out* prior is one that admits as plausible more datasets than a more concentrated one. This will be reflected in the computation of the above integral as you will get a smaller value with a wider prior than with a more concentrated prior.  

* **The bad: Computing the marginal likelihood is, generally, a hard task**. The above is an integral of a highly variable function over a high dimensional parameter space. In general this integral needs to be solved numerically using more or less sophisticated methods (see and example [here](https://docs.pymc.io/notebooks/Bayes_factor.html)).


* **The ugly: The marginal likelihood depends *sensitively* on the values of the priors**. Using the marginal likelihood to compare models is a good idea because a penalization for complex models is already included (thus preventing us from overfitting). At the same time, a change in the prior will affect the computations of the marginal likelihood. At first this sounds a little bit silly: we already know that priors affect computations (otherwise we could simply avoid them), but the point here is the word "sensitively". We are talking about changes in the prior that will keep inference of the parameters *more or less* the same, but could have a big impact on the value of the marginal likelihood. Another source of criticism to Bayes factors is that they can be used as a Bayesian way of doing hypothesis testing; there is  nothing wrong with this *per se*, but many authors have pointed out that an inference approach, similar to the one used in this book, is better suited to  most problems than the generally taught approach of hypothesis testing (whether  Bayesian or not Bayesian).

## Bayes Factors vs Information Criteria

WAIC/LOO uses the log-likelihood and the priors are not directly part of the computations -- they are indirectly included because they will have an effect on the values of the models parameters. Instead, Bayes factors use priors directly as we need to average the likelihood over the prior. Conceptually we can say that Bayes factors are focused on identifying the best model (and the prior is part of the model) while WAIC and LOO are focused on which parameters will give the best predictions. In most scenarios priors are used for their regularizing properties and, when possible, to provide some background knowledge -- more so than because we *really really believe* they reflect some *truth*. As a result, we think information criteria are a more robust approach in practice. Moreover, their computation is far less problematic and generally more robust, without the need to use special samplers or methods.