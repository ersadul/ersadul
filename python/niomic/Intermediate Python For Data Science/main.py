# %%
import matplotlib.pyplot as plt

# %%
year = [1950, 1970, 1990, 2010]
population = [2.519, 3.692, 5.263, 6.792]
plt.plot(year, population) # using line plot
#plt.scatter(year, population) # using scatter plot: one dot for each observation
plt.show()