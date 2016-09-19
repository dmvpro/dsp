[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)
```python
from __future__ import print_function

import thinkstats2
import thinkplot

import math
import random
import numpy as np

from scipy import stats
from estimation import RMSE, MeanError


def SimulateSample(lam=2, n=10, m=1000):
    """Sampling distribution of L as an estimator of exponential parameter.

    lam: parameter of an exponential distribution
    n: sample size
    m: number of iterations
    """
    def VertLine(x, y=1):
        thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)

    estimates = []
    for j in range(m):
        xs = np.random.exponential(1.0/lam, n)
        lamhat = 1.0 / np.mean(xs)
        estimates.append(lamhat)

    stderr = RMSE(estimates, lam)
    print('standard error', stderr)

    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print('confidence interval', ci)
    VertLine(ci[0])
    VertLine(ci[1])

    # plot the CDF
    thinkplot.Cdf(cdf)
    thinkplot.Save(root='estimation2',
                   xlabel='estimate',
                   ylabel='CDF',
                   title='Sampling distribution')

    return stderr

if __name__ == '__main__':
    main()
    
"""Exercise 8.2 Conclusions:

1) With sample size 10:

standard error 0.896717911545
confidence interval (1.2901330772324622, 3.8692334892427911)

2) As sample size increases, standard error and the width of
the CI decrease:

10      0.90    (1.3, 3.9)
100     0.21    (1.7, 2.4)
1000    0.06    (1.9, 2.1)

All three confidence intervals contain the actual value, 2."""
```
