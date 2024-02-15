from sense_hat import SenseHat
from ISStreamer.Streamer import Streamer
import time

# Instantiate a streamer object with your account access_key and a bucket_key (the bucket_key can be anything, just make it unique)
streamer = Streamer(

sense = SenseHat()
while True:
  orientation = sense.get_orientation()

  # Instead of printing the results of pitch, roll, and yaw to the screen, change this section to stream each value to your Initial State account
  print("Pitch = " + str(orientation['pitch']))
  print("Roll = " + str(orientation['roll'])) 
  print("Yaw = " + str(orientation['yaw']))

  # Flush the buffer, then go to sleep to ensure only 3 API calls per second
  streamer.flush()
  time.sleep(.333)

