from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

sense.clear()
sense.set_rotation(90)
rgb = []
col_start = 0
col_dir_left = True
while True:
  # Randomly turn on a blue pixel
  x_rand = randint(0,7)
  y_rand = randint(0,7)
  sense.set_pixel(x_rand,y_rand,0,0,128)
  sleep(.05)

  # Cycle through all pixels and find any white pixel that 
  # is on and clear it then turn on the pixel below it
  for x in range(8):
    for y in range(8):
      row = 7-x
      col = 7-y
      rgb = sense.get_pixel(row,col)
      if rgb[0] > 200 and rgb[1] > 200 and rgb[2] > 200:
        if row < 7:
          sense.set_pixel(row+1, col, 255, 255, 255)
        sense.set_pixel(row, col, 0, 0, 0)
  # Turn on a pixel at the top but move back and forth (left->right->left)
  if col_dir_left:
    if col_start < 7:
      col_start = col_start+1
    else:
      col_dir_left = False
  else:
    if col_start > 0:
      col_start = col_start-1
    else:
      col_dir_left = True
  sense.set_pixel(0, col_start, 255, 255, 255)
  sleep(.05)


