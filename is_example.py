from ISStreamer.Streamer import Streamer
from time import sleep

ACCESS_KEY = "PLACE YOUR INITIAL STATE ACCESS KEY HERE"
BUCKET_KEY = "pythontest"
BUCKET_NAME = "Python Test"

# create a Streamer instance
streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

print("Streaming data to Initial State ...")
for x in range(50):
  # send some data
  streamer.log("myNumber", x)
  sleep(.05)

# flush the stream
streamer.flush()
print("Streaming complete!")
