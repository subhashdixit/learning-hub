"""Check Bellman updates and Bayesian/GP arithmetic. Synthetic teaching example; no remote data required."""
import numpy as np
q=2.;reward=1.;discount=.9;next_best=4.;rate=.1
q_new=q+rate*(reward+discount*next_best-q);assert np.isclose(q_new,2.26)
prior_a=prior_b=1;successes=7;failures=3
posterior_mean=(prior_a+successes)/(prior_a+prior_b+successes+failures)
assert np.isclose(posterior_mean,2/3)
# One-point GP: kernel variance1, observation-noise variance.25.
mean=1/1.25;latent_variance=1-1/1.25
assert np.isclose(mean,.8) and np.isclose(latent_variance,.2)
print('Q update:',q_new,'Beta posterior mean:',posterior_mean,'GP mean/variance:',mean,latent_variance)
