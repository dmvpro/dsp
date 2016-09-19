[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)
```python
from __future__ import print_function

import thinkstats2
import thinkplot

import math
import random
import numpy as np

from scipy import stats
from estimation import RMSE, MeanError

def SimulateGame(lam):
    """Simulates a game and returns the estimated goal-scoring rate.

    lam: actual goal scoring rate in goals per game
    """
    goals = 0
    t = 0
    while True:
        time_between_goals = random.expovariate(lam)
        t += time_between_goals
        if t > 1:
            break
        goals += 1

    # estimated goal-scoring rate is the actual number of goals scored
    L = goals
    return L


def Estimate2(lam=2, m=1000000):

    estimates = []
    for i in range(m):
        L = SimulateGame(lam)
        estimates.append(L)

    print('Experiment 2')
    print('rmse L', RMSE(estimates, lam))
    print('mean error L', MeanError(estimates, lam))

    pmf = thinkstats2.Pmf(estimates)

    thinkplot.Hist(pmf)
    thinkplot.Show()


def main():
    thinkstats2.RandomSeed(17)

    Estimate2()

    print('Experiment 3')
    for n in [10, 100, 1000]:
        stderr = SimulateSample(n=n)
        print(n, stderr)


if __name__ == '__main__':
    main()

"""Exercise 8.3 Conclusions:

1) RMSE for this way of estimating lambda is 1.4

2) The mean error is small and decreases with m, so this estimator
appears to be unbiased.
"""
```
