# Given: A list of speeds
# Find: The walker with the fastest speed

# Modify!!! get list of speeds and list of walker names
# and print the name of the fastest walker

# Get speeds
speedList = []
walkerList = []

numWalkers = int(input("Enter number of walkers: "))

for i in range(numWalkers):
    speed = float(input("Enter speed: "))
    speedList.append(speed)
    walker = input("Enter walker name: ")
    walkerList.append(walker)

# Initialize high speed
high_speed = speedList[0]
fastest_walker = 0

# Find fastest speed
for i in range(len(speedList)):
    if speedList[i] > high_speed:
        high_speed = speedList[i]
        fastest_walker = i

# print highest speed
print("The fastest speed is ", high_speed)
print("The fastest walker is at position ", fastest_walker)
print("The name of the fastest walker is ", walkerList[fastest_walker]) 





"""


# Given n distances and times
# Find the fastest speed of all walkers

# Get number of walkers
num = int(input("How many walkers? "))

# Get distance and time for first walker
dist = int(input("Enter distance (miles): "))
time = int(input("Enter time (minutes): "))

# Compute speed for first walker
speed = dist/time

# Initialize fastest
fastest = speed

# Loop to compare with all other walkers' speeds

#Initialize counter
i = 1

# Initialize highspeed
highSpeed = speed
fastetWalker = 1

# Test counter
while i < num:
    
    # Get next time and distance
    dist = int(input("Enter distance (miles): "))
    time = int(input("Enter time (minutes): "))

    # Compute speed
    speed = dist/time

    # Compare speed with highSpeed
    if speed > highSpeed:
        highSpeed = speed

    # Increment counter
    i += 1

# convert fastest to MPH
fastest = fastest * 60

print ("The fastest speed is: ", fastest, "mph")


"""
