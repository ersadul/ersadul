# 3. 
import matplotlib.pyplot as plt

#%%
year = [1950, 1951, 1952, 2100]
population = [2.538, 2.57, 2.62, 10.85]

year = [1800, 1850, 1900] + year
population = [1.0, 1.262, 1.650] + population

plt.plot(year, population)
plt.xlabel('Year') # labeling for x axis
plt.ylabel('Population') # labeling for y axis
plt.yticks([0, 2, 4, 6, 8, 10], [0, '2B', '4B', '6B', '8B', '10B'])
plt.title('World Population')
plt.show()