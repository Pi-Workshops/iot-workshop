from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

humidity = sense.get_humidity()
temp_c = sense.get_temperature()



# Two problems: 1) the temperature is in Celsius and 2) both values print out to eight decimal places. 
# Convert the temperature to Fahrenheit.
# Format the output to two decimal places. 
# Print the result of both values.
# Scroll the temperature value to the LED matrix.
# Make the screen flash using the warning function if > a specific temperature

