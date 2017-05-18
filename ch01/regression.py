#The task is to find the number of weeks before our infrastructure has 100000 hits, so as to prepare for change of a server.
#Change the current working direcory
import os
os.chdir('C:\\Users\\satis\\Desktop\\Summer ML\\Mine\\ch01')

import scipy as sp
data = sp.genfromtxt("web_traffic.tsv", delimiter = "\t")

#Dividing data into two columns
x = data[:,0]
y = data[:,1]

#Remove data that has nans in them
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

#Plotting the data
import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()

#############################################

def error(f,x,y):
    return sp.sum((f(x)-y)**2)

inflection = int(3.5*7*24) # calculate the inflection point in hours
xa = x[:inflection] # data before the inflection point
ya = y[:inflection]
xb = x[inflection:] # data after
yb = y[inflection:]
fa = sp.poly1d(sp.polyfit(xa, ya, 2))
fb = sp.poly1d(sp.polyfit(xb, yb, 2))
fa_error = error(fa, xa, ya)
fb_error = error(fb, xb, yb)
print("Error inflection=%f" % (fa_error + fb_error))

from scipy.optimize import fsolve
reached_max = fsolve(fb-100000,800)/(7*24)
print("The time to reach 100000 hits is: %f" % reached_max[0])
