import ultrasonic
from time import sleep
#from machine import Pin
from motor import Motor

motor_left = Motor("left", "D6", "D7", "D4")
motor_right = Motor("right", "D8", "D9", "D5")

print("Hello, world!")  # Print a welcome message on reset

# These statements make the code more readable.
# Instead of a pin number "D13" or "D12" we can now write "TRIG" or "ECHO"
TRIG = "D13"
ECHO = "D12"
ultrasonic_sensor = ultrasonic.HCSR04(TRIG, ECHO)

while True:
    dist = ultrasonic_sensor.distance_mm()

    if dist >= 60:
        print('if')
        #motor_left.ctrl_alloc(1, 70)
        #motor_right.ctrl_alloc(1, 70)

        motor_left.set_forwards()
        motor_right.set_forwards()

        motor_left.duty(90)
        motor_right.duty(90)
        sleep(0.1)

        motor_left.duty(20)
        motor_right.duty(20)

    elif dist <= 60:
        print('elif')
        #motor_left.ctrl_alloc(0, 70)
        #motor_right.ctrl_alloc(0, 70)

        motor_left.set_backwards()
        motor_right.set_backwards()

        motor_left.duty(90)
        motor_right.duty(90)
        sleep(0.1)

        motor_left.duty(30)
        motor_right.duty(30)


    # if dist <= 100:
    # motor_left.duty(0)
    # motor_right.duty(0)
    # else:
    # motor_left.setforwards()
    # motor_right.setforwards()
    # motor_left.duty(50)
    # motor_right.duty(50)

    #if dist < 200:
        # The code within this if-statement only gets executed
        # if the distance measured is less than 200 mm
        #print("Distance = {:6.2f} [mm]".format(dist))
    sleep(0.1)
