from sense_hat import SenseHat

sense = SenseHat()

while True:
  orientation = sense.get_orientation()
  
  print("Pitch = " + str(orientation['pitch']))
  print("Roll = " + str(orientation['roll']))
  print("Yaw = " + str(orientation['yaw']))

