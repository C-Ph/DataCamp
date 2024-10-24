# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]


# Change for loop to use enumerate() and update print()
for index, height  in enumerate(areas) :
    print("room" + str(index) + ": " + str(height))

#----------------------------------------------------------------------------------------------

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]

# Build a for loop from scratch
for room in house:
    name = room[0]
    area = room[1]
    print("the " + str(name) + " is " + str(area) + " sqm")
    #print(f"The {name} is {area} sqm.")

