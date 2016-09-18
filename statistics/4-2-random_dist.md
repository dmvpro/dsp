[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```python
import thinkstats2
import thinkplot
import random
import scipy.stats

#construct & plot random PMF
t = [random.random() for _ in range(1000)]
pmf = thinkstats2.Pmf(t)
thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.Show()

#construct & plot random CDF
cdf = thinkstats2.Cdf(t)
thinkplot.Cdf(cdf)
thinkplot.Show()

#calculate uniformity
print scipy.stats.norm.cdf(0)
```
