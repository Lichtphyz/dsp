[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>Input:
```
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

print("Mean first born baby weight =", firsts.totalwgt_lb.mean())
print("Mean non-first born baby weight =", others.totalwgt_lb.mean())
print("Weight Difference (first - other) =", \
      `firsts.totalwgt_lb.mean()-others.totalwgt_lb.mean())

print('Cohen\'s D:', CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb))
```
>Output:
```
Mean first born baby weight = 7.201094430437772
Mean non-first born baby weight = 7.325855614973262
Weight Difference (first - other) = -0.12476118453549034
Cohen's D: -0.0886729270726'
```
