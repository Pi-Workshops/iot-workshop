import math

# Write a function to compute a single length of face diagonal calculation
# The function should have two input parameters and return a calculated value

# Dimensions of box 1
length1 = 21
width1 = 16
height1 = 46
volume1 = length1 * width1 * height1

# Dimensions of box 2
length2 = 18
width2 = 22
height2 = 43
volume2 = length2 * width2 * height2

# Minimum and maximum volumes
min_volume = min(volume1, volume2)
max_volume = max(volume1, volume2)

# Maximum : minimum ratio
ratio = max_volume/min_volume

# Print the ratio, round to one decimal place
print("The ratio of max to min volume is " + format(ratio, ".1f"))

# Call the length of face diagonal calculation function for each value
d_lw1 =
d_lh1 =
d_hw1 =

print("The lengths of face diagonals of box 1 are " + format(d_lw1, ".1f") + ", " + format(d_lh1, ".1f") + ", " + format(d_hw1, ".1f"))

