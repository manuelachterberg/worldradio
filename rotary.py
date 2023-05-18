import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the rotary encoder
encoder_pinA = 17
encoder_pinB = 27
switch_pin = 22

# Set up encoder pins as inputs with pull-up resistors
GPIO.setup(encoder_pinA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(encoder_pinB, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize variables
counter = 0
prev_counter = 0

# Define a callback function for the encoder rotation
def encoder_callback(channel):
    global counter, prev_counter
    time.sleep(0.002)  # Debounce delay
    if GPIO.input(encoder_pinB):
        counter += 1
    else:
        counter -= 1

# Add event detection for encoder rotation
GPIO.add_event_detect(encoder_pinA, GPIO.FALLING, callback=encoder_callback, bouncetime=10)

# Run the script indefinitely
try:
    while True:
        if counter != prev_counter:
            print("Counter value:", counter)  # Perform actions based on counter value
            prev_counter = counter
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
