import numpy as np
import matplotlib.pyplot as pp
from scipy.stats import norm

def df_mean(x):
    xmean = np.mean(x)
    return [xi - xmean for xi in x]


def covariance(x, y):
    n = len(x)
    return np.dot(df_mean(x), df_mean(y)) / (n-1)

pageSpeed = np.random.normal(3.0, 1.0, 1000)
purchaseAmount1 = np.random.normal(50.0, 10, 1000)
pp.scatter(pageSpeed, purchaseAmount1)
covariance(pageSpeed, purchaseAmount1)

purchaseAmount = np.random.normal(50.0, 10, 1000) / pageSpeed
pp.scatter(pageSpeed, purchaseAmount)
covariance(pageSpeed, purchaseAmount)

pp.show()
    