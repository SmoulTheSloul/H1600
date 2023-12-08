from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time
import argparse  
parser = argparse.ArgumentParser()
parser.add_argument('--connect', default='/dev/ttyUSB0')
args = parser.parse_args()

# Connect to the Vehicle
print 'Connecting to vehicle on: %s' % args.connect
vehicle = connect(args.connect, baud=921600, wait_ready=True)


print("Connection to Cube Orange Succesful!")
print("Mode: %s" % vehicle.mode.name)
time.sleep(2)
# Close vehicle object before exiting script
vehicle.close()

print("Completed")
