# NumPy is imported; seed is set
import numpy as np
np.random.seed(123)

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk five times
for i in range(5) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)

#----------------------------------------------------------------------------------------------

# numpy and matplotlib imported, seed set.
import numpy as pd
import matplotlib.pyplot as plt
np.random.seed(123)

# initialize and populate all_walks
all_walks = []
for i in range(5) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.title("Random Walks")
plt.xlabel("Steps")
plt.ylabel("Position")
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.title("Random Walks Transposed")
plt.xlabel("Throw Number")
plt.ylabel("Position")
plt.show()

#----------------------------------------------------------------------------------------------

# numpy and matplotlib imported, seed set
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)

# clear the plot so it doesn't get cluttered if you run this many times
plt.clf()

# Simulate random walk 20 times
all_walks = []
for i in range(20) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.005 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()


#----------------------------------------------------------------------------------------------

# numpy and matplotlib imported, seed set
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)


# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1, :]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.title("Histogram of Random Walk Endpoints")
plt.xlabel("Endpoint Position")
plt.ylabel("Frequency")
plt.show()

#----------------------------------------------------------------------------------------------

'''Calculate the odds
The histogram of the previous exercise was created from a NumPy array ends, that contains 500 integers. 
Each integer represents the end point of a random walk. To calculate the chance that this end point is greater than or equal to 60,
 you can count the number of integers in ends that are greater than or equal to 60 and divide that number by 500, 
 the total number of simulations.

Well then, what's the estimated chance that you'll reach at least 60 steps high if you play this Empire State Building game? 
The ends array is everything you need; it's available in your Python session so you can calculate it.'''

count_greater_equal_60 = np.sum(ends >= 60)  

estimated_chance = count_greater_equal_60 / 500  

print(estimated_chance)  

0.784