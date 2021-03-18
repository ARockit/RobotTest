# Reads repeatedly from an analog input and calculates a running average
import numpy as np
import time

# Number of readings to be used in the readings array
num_readings = 10

readings = np.zeros(num_readings)  # Array to be used to store value of readings
read_index = 0
total = 0
average = 0


# This is a stub meant to replicate a sensor reading
def sensorRead():
    return np.random.random(1)


while True:
    # Subtract the last reading
    total = total - readings[read_index]
    # Read from the sensor
    readings[read_index] = sensorRead()
    print(readings)
    # Add the reading to the total
    total = total + readings[read_index]
    # Advance to the next position in the array
    read_index = read_index + 1

    # if at the end of the array
    if read_index >= num_readings:
        # wrap around to the beginning of the array
        read_index = 0

    # Calculate the average
    average = total/num_readings
    print(average)
    time.sleep(1)