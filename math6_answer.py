import math

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

# Box 1 length of face diagonal calculation
d_lw1 = math.sqrt(pow(length1,2) + pow(width1,2))
d_lh1 = math.sqrt(pow(length1,2) + pow(height1,2))
d_hw1 = math.sqrt(pow(height1,2) + pow(width1,2))

print("The lengths of face diagonals of box 1 are " + format(d_lw1, ".1f") + ", " + format(d_lh1, ".1f") + ", " + format(d_hw1, ".1f"))
 

