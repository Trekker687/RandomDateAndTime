import random
import time

def randomdate(startdate, enddate):
    print("Printing random date between", startdate, "and", enddate)
    randomGen = random.random()
    dateformat = "%d/%m/%y"
    
    starttime = time.mktime(time.strptime(startdate.strip(),dateformat))
    endtime = time.mktime(time.strptime(enddate.strip(),dateformat))
    randomtime = starttime + randomGen * (endtime - starttime)
    randomdate = time.strftime(dateformat, time.localtime(randomtime))
    return randomdate


print("Random date = ", randomdate("01/01/2010","16/12/2024"))
