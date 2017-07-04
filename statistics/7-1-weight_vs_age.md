[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

```
import first

live, firsts, others = first.MakeFrames()
live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
```

```
#weights = live.birthwgt_lb + live.birthwgt_oz/16
weights = live.totalwgt_lb
ages = live.agepreg
thinkplot.Scatter(ages, weights, alpha=1)
thinkplot.Config(xlabel='Age (years)',
                 ylabel='Weight (kg)',
                 legend=False)
```
```
thinkplot.HexBin(ages, weights)
thinkplot.Config(xlabel='Age (years)',
                 ylabel='Weight (kg)',
                 legend=False)
```
```
bins = np.arange(10, 60, 2)
#print(bins)
indices = np.digitize(ages, bins)
#print(indices)
groups = live.groupby(indices)
#print(groups)
#for i, group in groups:
#    print(i, len(group))
mean_ages = [group.agepreg.mean() for i, group in groups]
#print(mean_ages)
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]
for percent in [75, 50, 25]:
    weight_percentiles = [cdf.Percentile(percent) for cdf in cdfs]
    label = '%dth' % percent
    thinkplot.Plot(mean_ages, weight_percentiles, label=label)

thinkplot.Config(xlabel='Ages (years)',
                 ylabel='Weight (kg)',
                 #axis=[10, 70, 0, 16],
                 legend=False)
```
```
#again for a smaller range of values, to exclude intervals with too 
#little data (less than 5 data points)
bins = np.arange(14, 42, 2)
indices = np.digitize(ages, bins)
groups = live.groupby(indices)
mean_ages = [group.agepreg.mean() for i, group in groups]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]
for percent in [75, 50, 25]:
    weight_percentiles = [cdf.Percentile(percent) for cdf in cdfs]
    label = '%dth' % percent
    thinkplot.Plot(mean_ages, weight_percentiles, label=label)

thinkplot.Config(xlabel='Ages (years)',
                 ylabel='Weight (kg)',
                 #axis=[10, 70, 0, 16],
                 legend=False)
```
```
np.corrcoef(ages, weights)[1][0]
```
0.068833970354109097
```
SpearmanCorr(ages, weights)
```
0.094610041096582262
