import numpy as np
import matplotlib.pyplot as pp

incomes = np.random.normal(100.0, 20.0, 10000)
print(incomes)
pp.hist(incomes, 50)
pp.show()
print(incomes.std())
print(incomes.var())