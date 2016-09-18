[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)
```python
from __future__ import print_function, division

import scipy.stats

%matplotlib inline

# scipy.stats.norm = normal distribution
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)

# frozen random variable can compute its mean & std
dist.mean(), dist.std()

# cdf displays that ~16% of people are 1 std below the mean
dist.cdf(mu-sigma)

# define and dislpay upper and lower criteria in cm and calculate difference 
low = dist.cdf(177.8)    # 5'10"
high = dist.cdf(185.4)   # 6'1"
print(high-low)

# Conclusion: ~34.2% of US male population meets Blue Man Group casting height criteria
```
