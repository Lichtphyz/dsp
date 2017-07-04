[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

---
>> My code for Chapter 8, exercise 3:
```
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
```
```
def Q3(lam = 2, games = 1000000):
    
    est = []
    for i in range(games):
        est += [SimulateGame(lam)]
    print("RMSE of L = ",RMSE(est,lam))
    print("Mean Error L = ",MeanError(est,lam))
    
    pmfL = thinkstats2.Pmf(est)
    thinkplot.Hist(pmfL)
    thinkplot.Config(xlabel="Goals per game",ylabel="PMF")
    
Q3()
```
Output:
RMSE of L =  1.41368949915
Mean Error L =  0.000624

>RMSE for L is about 1.41.  The Mean Error in L is relatively small,
Fluxuates positive and negative, and gets closer to zero as the number
of games is increased.  **This suggest this estimator is unbiased**.

---
