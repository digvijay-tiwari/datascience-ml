import numpy as np
import matplotlib.pyplot as pp
from scipy.stats import norm

def df_mean(x):
    xmean = np.mean(x)
    return [xi - xmean for xi in x]

def covariance(x, y):
    n = len(x)
    return np.dot(df_mean(x), df_mean(y)) / (n-1)

def correlation(x, y):
    stdevx = x.std()
    stdevy = y.std()
    return covariance(x, y) / stdevx / stdevy


pageSpeed = np.random.normal(3.0, 1.0, 1000)

# Calculate random correlation
purchaseAmount = np.random.normal(50.0, 10, 1000) / pageSpeed
pp.scatter(pageSpeed, purchaseAmount)
print(correlation(pageSpeed, purchaseAmount))
print(np.corrcoef(pageSpeed, purchaseAmount))

# Calculate perfect correlation
purchaseAmountperfect = 100 - pageSpeed * 4
pp.scatter(pageSpeed, purchaseAmountperfect)
print(correlation(pageSpeed, purchaseAmountperfect))
print(np.corrcoef(pageSpeed, purchaseAmountperfect))
pp.show()