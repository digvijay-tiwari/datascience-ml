import numpy as np
import matplotlib.pyplot as pp
from scipy.stats import norm

incomes = np.random.uniform(-10.0, 10.0, 10000)
print(incomes)
pp.hist(incomes, 50)
pp.show()

x = np.arange(-3, 3, 0.001)
pp.plot(x, norm.pdf(x))
pp.show()