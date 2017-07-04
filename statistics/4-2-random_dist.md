[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```
import numpy
random_set = [numpy.random.uniform(0,100) for x in range(1000)]

Rpmf = thinkstats2.Pmf(random_set, label='random numbers 0-100')
thinkplot.Hist(Rpmf, align='right', width=width)
```

This PMF is clearly not uniform, but it instead has a value of 1/n on all of the numbers which were randomly selected, and 0. elsewhere.  It represents the PMF of THIS set of numbers, not of random numbers yet to be determined.  We do not have a good way to measure the PMF before the numbers were selected.

Now for the CDF:

```
Rcdf = thinkstats2.Cdf(random_set, label='random numbers 0-100')
thinkplot.Cdf(Rcdf)
thinkplot.Config(xlabel='Percentile rank', ylabel='CDF')
```
The CDF however is quite uniform.
