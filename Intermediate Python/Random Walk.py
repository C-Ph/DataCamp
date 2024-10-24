''' Make a list `random_walk` that contains the first step, which is the integer 0.
- Finish the `for` loop:
- The loop should run `100` times.
- On each iteration, set `step` equal to the last element in the `random_walk` list. You can use the index `-1` for this.
- Next, let the `if`-`elif`-`else` construct update `step` for you.
- The code that appends `step` to `random_walk` is already coded.
- Print out `random_walk`.'''

# NumPy is imported, seed is set
import numpy as np
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]
    
    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)


#----------------------------------------------------------------------------------------------
'''- Use `max()` in a similar way to make sure that `step` doesn't go below zero if `dice <= 2`.
- Hit _Submit Answer_ and check the contents of `random_walk`.'''
# NumPy is imported, seed is set
import numpy as np
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
        #step = step - 1 #Original
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)
    random_walk.append(step)
print(random_walk)

#----------------------------------------------------------------------------------------------

# NumPy is imported, seed is set
import numpy as np
np.random.seed(123)

# Initialization
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


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()

'''[0, 3, 4, 5, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 6, 5,
 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 8, 9, 10, 11, 12, 11, 15, 
 16, 15, 16, 15, 16, 17, 18, 19, 20, 21, 22, 25, 26, 27, 
 28, 33, 34, 38, 39, 38, 39, 40, 39, 40, 41, 43, 44, 45, 
 44, 43, 44, 45, 44, 43, 44, 45, 47, 46, 45, 46, 45, 46, 
 47, 48, 50, 49, 50, 51, 52, 53, 54, 53, 52, 53, 52, 53, 
 54, 53, 56, 57, 58, 59, 58, 59, 60]'''
