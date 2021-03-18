from time import sleep
from motor import Motor
from encoder import Encoder

# Create left and right ‘Motor’ objects
motor_left = Motor("left", "D6", "D7", "D4")
motor_right = Motor("right", "D8", "D9", "D5")
# Create encoder object
ENC_L = "D2"
ENC_R = "D3"
enc = Encoder(ENC_L, ENC_R)
enc_desired_counts = 29.4

while True:
    motor_left.set_forwards()  # Set the left motor to run forwards
    motor_right.set_forwards()  # Set the right motor to run forwards
    enc.clear_count()  # Reset the encoder to zero

    # Drive until average counts exceed a value
    while (enc.get_left() + enc.get_right()) / 2 < enc_desired_counts:
        motor_left.duty(80)  # Set the left motor to 80% pwm forwards
        motor_right.duty(80)  # Set the right motor to 80% pwm forwards
        # Stop the motors for 1s
        motor_left.duty(0)
        motor_right.duty(0)
        sleep(1)

        # Clear encoder count and set direction pins for backwards
        enc.clear_count()
        motor_left.set_backwards()
        motor_right.set_backwards()

        # Drive until average counts exceed a value
        while (enc.get_left() + enc.get_right()) / 2 < enc_desired_counts:
            motor_left.duty(80)  # Set the left motor to 80% pwm backwards
            motor_right.duty(80)  # Set the left motor to 80% pwm backwards

        sleep(1)