import math

# Length of face diagonal calculation
def len_of_face(x, y):
  return math.sqrt(pow(x,2) + pow(y,2))

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
d_lw1 = len_of_face(length1, width1)
d_lh1 = len_of_face(length1, height1)
d_hw1 = len_of_face(height1, width1)

print("The lengths of face diagonals of box 1 are " + format(d_lw1, ".1f") + ", " + format(d_lh1, ".1f") + ", " + format(d_hw1, ".1f"))

