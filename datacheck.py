#%matplotlib inline
import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as numpy
import pandas as pd
from scipy import stats

lan = pd.read_csv('languages.csv')
langCount = lan['language'].value_counts()

#print(langCount.plot(kind='bar'))

income = numpy.random.normal(27000, 15000, 10000)
#income = numpy.append(income, [1000000000])
print(numpy.mean(income))
print(numpy.median(income))

plt.hist(income, 50)
plt.show()

ages = numpy.random.randint(18, high=90, size=1000)
print(stats.mode(ages))
print(stats.mode(ages).mode[0])


