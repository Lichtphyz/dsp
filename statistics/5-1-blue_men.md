[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

#Answer:

*Kind of overkill on this one, but I realized there were multiple interpretations of the questions, so I tried answering it several different ways.*

```
import brfss
import scipy.stats
df = brfss.ReadBrfss()
```
First, according to the (normal) model, how many men 'should' be between 5'10" and 6'1'?
```
dfm = df[df.sex == 1]
heights = dfm.htm3.dropna()
mu = heights.mean()
sig = heights.std()
min_h_cm = (5*12+10)*2.54
max_h_cm = (6*12+1)*2.54
#from docs:  cdf(x, loc=0, scale=1)
under = scipy.stats.norm.cdf(min_h_cm,mu,sig)
over = 1 - scipy.stats.norm.cdf(max_h_cm,mu,sig)
print("% too short =",under," %too tall =",over)
Blue_Qualify = 1 - under - over
print(Blue_Qualify,"% of men expected meet the height requirement for Blue Man Group")
```
#returns:

*% too short = 0.486251705841  %too tall = 0.170517417722
0.343230876437 % of men expected meet the height requirement for Blue Man Group*

Alternate interpretation: how many of the people surveyed fall within the heigth range (sex neglected)?

```
heights = df.htm3.dropna()
npeople= len(heights)
tall_enough = heights[heights >= (5*12+10)*2.54]
but_not_too_tall = tall_enough[tall_enough <= (6*12+1)*2.54]
Blue_Qualify_data = len(but_not_too_tall)
print(Blue_Qualify_data,"% out of",npeople,\
      "people surveyed meet the height requirement for Blue Man Group")
print("This is ",100*Blue_Qualify_data/npeople,"% of the population")
```
#returns:

*81453 % out of 409129 people surveyed meet the height requirement for Blue Man Group
This is  19.908879595433227 % of the population*

For comparision, here is the same thing for males only

```
heights = dfm.htm3.dropna()
npeople= len(heights)
tall_enough = heights[heights >= (5*12+10)*2.54]
but_not_too_tall = tall_enough[tall_enough <= (6*12+1)*2.54]
Blue_Qualify_data = len(but_not_too_tall)
print(Blue_Qualify_data,"% out of",npeople,\
      "men surveyed meet the height requirement for Blue Man Group")
print("This is ",100*Blue_Qualify_data/npeople,"% of the Male population")
```
#returns:

*73697 % out of 154407 men surveyed meet the height requirement for Blue Man Group
This is  47.729053734610474 % of the Male population*

>>Note that the two methods give rather different answers.  Either our survey does not represent a random sample of the population, or the population is not modeled especially well by a normal distribution (perhaps log-normal would be better).
