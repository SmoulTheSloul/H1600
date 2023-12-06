from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--connect', default='/dev/ttyUSB0')
args = parser.parse_args()

# Connect to the Vehicle
print('Connecting to vehicle on: %s' % args.connect)
vehicle = connect(args.connect, baud=921600, wait_ready=True)

print("Connection to Cube Orange Successful!")
print("Mode: %s" % vehicle.mode.name)

# Function to send a text message
def send_text_message(message):
    # Create a MAVLink message for sending text messages
    msg = vehicle.message_factory.statustext_encode(
        severity=mavutil.mavlink.MAV_SEVERITY_INFO,
        text=message
    )

    # Send the message
    vehicle.send_mavlink(msg)

# Example usage
try:
    # Send a text message
    send_text_message("Hello from Raspberry Pi!")

    # Wait for a few seconds (optional)
    time.sleep(5)

finally:
    # Close vehicle object before exiting script
    vehicle.close()
    print("Completed")
