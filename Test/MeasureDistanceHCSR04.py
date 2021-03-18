import ultrasonic
from time import sleep

print("Hello, world!")  # Print a welcome message on reset

# These statements make the code more readable.
# Instead of a pin number "D13" or "D12" we can now write "TRIG" or "ECHO"
TRIG = "D13"
ECHO = "D12"
ultrasonic_sensor = ultrasonic.HCSR04(TRIG, ECHO)

while True:
    dist = ultrasonic_sensor.distance_mm()
    if dist < 200:
        # The code within this if-statement only gets executed
        # if the distance measured is less than 200 mm
        print("Distance = {:6.2f} [mm]".format(dist))
    sleep(0.1)