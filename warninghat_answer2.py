from sense_hat import SenseHat
from time import sleep

def warning_flash():
  r  = [255, 0, 0]  
  w = [255, 255, 255]  
  
  red_screen = []
  for p in range(0,64):
    red_screen.append(r)

  white_screen = []
  for p in range(0,64):
    white_screen.append(w)

  for x in range(0,10):
    sense.set_pixels(white_screen)
    sleep(0.5)
    sense.set_pixels(red_screen)
    sleep(0.5)
  return

sense = SenseHat()
warning_flash()

