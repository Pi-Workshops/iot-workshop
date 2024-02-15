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

humidity = sense.get_humidity()
temp_c = sense.get_temperature()


temp_f = format(temp_c * 9.0 / 5.0 + 32.0,".2f")
humidity = format(sense.get_humidity(), ".2f")
print("Temperature = " + temp_f)
print("Humidity = " + humidity)
sense.show_message(temp_f)

if float(temp_f) > 75:
  warning_flash()

