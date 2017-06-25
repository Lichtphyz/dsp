[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

**Python Code I used at the end of *chap03ex.ipynb* **
```
#load data
resp = nsfg.ReadFemResp()

#construct and plot historgram from entire data set, note +1 addition to account for baby just born
hist = thinkstats2.Hist(resp.numkdhh+1, label='actual') #+1 to include newborn baby
thinkplot.Hist(hist)
thinkplot.Config(xlabel='Children in Family', ylabel='Count')

#construct and plot a Probability Mass Function from the histrogram
pmf = thinkstats2.Pmf(hist)
thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='Children in Family', ylabel='Pmf')

#construct and plot the 'child biased' PMF (using the ThinkStats2 function BiasPmf,
#which multiplies each frequency by the number of children in the family
B_pmf = BiasPmf(pmf,label = 'observed by mothers')
thinkplot.Pmf(B_pmf)
thinkplot.Config(xlabel='Children in Family', ylabel='Biased_Pmf')

#plot both PMFs together
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, B_pmf])
thinkplot.Config(xlabel='Children in Family', ylabel='PMF')

#find mean values from PMFs and their difference
print("Actual mean =",pmf.Mean(),"children")
print("Biased mean =",B_pmf.Mean(),"children")
print("Over-estimation of the mean =", B_pmf.Mean()-pmf.Mean(),"children")
```
>*Output of final print statements:*
```
Actual mean = 2.02420515504 children
Biased mean = 2.72218990369 children
Over-estimation of the mean = 0.697984748647 children
```
