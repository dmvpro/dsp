[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)
```python
"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np

import hinc
import thinkplot
import thinkstats2
import density
from scipy.stats import skew

def InterpolateSample(df, log_upper=6.0):
    """Makes a sample of log10 household income.

    Assumes that log10 income is uniform in each range.

    df: DataFrame with columns income and freq
    log_upper: log10 of the assumed upper bound for the highest range

    returns: NumPy array of log10 household income
    """
    # compute the log10 of the upper bound for each range
    df['log_upper'] = np.log10(df.income)

    # get the lower bounds by shifting the upper bound and filling in
    # the first element
    df['log_lower'] = df.log_upper.shift(1)
    df.log_lower[0] = 3.0

    # plug in a value for the unknown upper bound of the highest range
    df.log_upper[41] = log_upper

    # use the freq column to generate the right number of values in
    # each range
    arrays = []
    for _, row in df.iterrows():
        vals = np.linspace(row.log_lower, row.log_upper, row.freq)
        arrays.append(vals)

    # collect the arrays into a single sample
    log_sample = np.concatenate(arrays)
    return log_sample

#create function to provide statistics on skew strength
def main():
    df = hinc.ReadData() #create DataFrame & InterpolateSample
    log_sample = InterpolateSample(df, log_upper=6.0)

    #define & plot CDF of sample
    log_cdf = thinkstats2.Cdf(log_sample)
    thinkplot.Cdf(log_cdf)
    thinkplot.Show(xlabel='household income',
                   ylabel='CDF')

    #calculate mean & median of the sample
    sample = np.power(10, log_sample)
    mean, median = density.Summarize(sample)
    std = np.std(sample)
    print('mean', mean)
    print('median', median)
    print('std', std)

    #calculate CDF of mean
    cdf = thinkstats2.Cdf(sample)
    print('cdf[mean]', cdf[mean])

    #define and plot PDF of sample
    pdf = thinkstats2.EstimatedPdf(sample)
    thinkplot.Pdf(pdf)
    thinkplot.Show(xlabel='household income', ylabel='PDF')

    #calculate skewness & Pearson's skewness
    skwns = skew(sample)
    Pskwns = 3 * (mean - median) / std
    print ('skewness', skwns)
    print ('Pearson\'s skewness', Pskwns)

if __name__ == "__main__":
    main()

'''Results
With log_upper=6.0 (assuming the largest income is $10^6):

mean 74278.7075312
std 93946.9299635
median 51226.4544789
skewness 4.94992024443
Pearson's skewness 0.736125801914
cdf[mean] 0.660005879567

Roughly 63% of households report a taxable income below the mean.

Results dependent on upper bound (eg: log_upper=7.0):

mean 124267.397222
std 559608.501374
median 51226.4544789
skewness 11.6036902675
Pearson's skewness 0.391564509277
cdf[mean] 0.856563066521

With an increase in the upper bound:
Skewness increases, but Pearson's decreases.
Mean increases 67%, but std increases almost 500%!
'''
```
