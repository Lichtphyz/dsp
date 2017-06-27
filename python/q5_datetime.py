# Hint:  use Google to find python function

####a) 
from datetime import datetime

date_start = '01-02-2013'  
date_stop = '07-28-2015'   

t1 = datetime.strptime(date_start, '%m-%d-%Y')
t2 = datetime.strptime(date_stop,  '%m-%d-%Y')  

dt = t2 - t1
print('days between 1st start and stop dates =', dt.days)

####b)  
date_start = '12312013'  
date_stop = '05282015'  

t3 = datetime.strptime(date_start, '%m%d%Y')
t4 = datetime.strptime(date_stop,  '%m%d%Y')  

dt = t4 - t3
print('days between 2nd start and stop dates =', dt.days)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

t5 = datetime.strptime(date_start, '%d-%b-%Y')
t6 = datetime.strptime(date_stop,  '%d-%b-%Y')  

dt = t6 - t5
print('days between 3nd start and stop dates =', dt.days)


""" Hackerrank Solution:
    
def difference_in_days(date1, date2):
    from datetime import datetime

    #date_start = '01-02-2013'  
    #date_stop = '07-28-2015'   

    t1 = datetime.strptime(date1, '%m-%d-%Y')
    t2 = datetime.strptime(date2, '%m-%d-%Y')  

    return (t2 - t1).days
    
    """