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

# Compute and print the length of face diagonals for box 1: 
# d_lw = square root (length^2 + width^2)
# d_lh = square root (length^2 + height^2)
# d_hw = square root (height^2 + width^2)

