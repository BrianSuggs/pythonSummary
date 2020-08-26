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
