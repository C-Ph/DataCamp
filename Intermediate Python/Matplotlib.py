import matplotlib.pyplot as plt

# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')


# Show plot
plt.show()

#----------------------------------------------------------------------------------------------------

#Build histogram with 5 bins
import matplotlib.pyplot as plt
plt.hist(life_exp, bins = 5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins = 20)

# Show and clean up again
plt.show()
plt.clf()

#----------------------------------------------------------------------------------------------------

# Histogram of life_exp, 15 bins
import matplotlib.pyplot as plt
plt.hist(life_exp, bins = 15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, bins = 15)

# Show and clear plot again
plt.show()
plt.clf()