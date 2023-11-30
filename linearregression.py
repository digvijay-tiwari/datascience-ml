import numpy as np
import matplotlib.pyplot as pp
from scipy import stats

def predictCorrect(x, slope, intercept):
    return slope * x + intercept


pageSpeed = np.random.normal(3.0, 1.0, 1000)

purchaseAmount = 100 - (pageSpeed + np.random.normal(0, 0.1, 1000)) * 4

slope, intercept, rvalue, pvalue, stderr = stats.linregress(pageSpeed, purchaseAmount)

linerline = predictCorrect(pageSpeed, slope=slope, intercept=intercept)

pp.scatter(pageSpeed, purchaseAmount)
pp.plot(pageSpeed, linerline, c="r")
pp.show()