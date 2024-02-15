from sense_hat import SenseHat
from ISStreamer.Streamer import Streamer
import time

streamer = Streamer(bucket_name="Movement Stream", bucket_key="random_moves", access_key="[Your Access Key]")

sense = SenseHat()
while True:
  orientation = sense.get_orientation()

  streamer.log("pitch", str(orientation['pitch']))
  streamer.log("roll", str(orientation['roll']))
  streamer.log("yaw", str(orientation['yaw']))
    
 # Flush the buffer, then go to sleep to ensure only 3 API calls per second
  streamer.flush()
  time.sleep(.333)

