[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

>> ```
def EstimateQ2(n=10, iters=1000):
    lam = 2

    Ls = []

    for _ in range(iters):
        xs = np.random.exponential(1.0/lam, n)
        L = 1 / np.mean(xs)
        Ls.append(L)

    cdf = thinkstats2.Cdf(Ls)
    thinkplot.Cdf(cdf)
    thinkplot.Config(xlabel='L Estimate',
                 ylabel='CDF')

    #print("Mean of the Ls",np.mean(means))
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print("90% confidence interval = ",ci)
    
    print('Standard Error in L', RMSE(Ls, lam))
    return RMSE(Ls, lam)
    
EstimateQ2()
```

Output:
```
90% confidence interval =  (1.2742649495275002, 3.5927008049765674)
Standard Error in L 0.781721734204
(and a graph of the CDF)
```

2nd part:
```
N = range(5,100)
MeanLs = []
for num in N:
    MeanLs += [EstimateQ2(num, iters=1000)]
thinkplot.Plot(N, MeanLs)
    
thinkplot.Config(title='RMSE vs n', xlabel='size of sample (n)', ylabel='RMSE', 
                 loc='lower right')
```

Output:

*a bunch of confidence and error statements, and a graph of RMSE vs Sample size(n).  The graph decays towards 0 as n increases.  It looks very roughly inversely proportional.
