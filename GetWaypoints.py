from dronekit import connect, VehicleMode
import time

# Connect to the Vehicle
vehicle = connect('/dev/ttyUSB0', baud=921600, wait_ready=True)

# Function to print mission waypoints
def print_mission():
    # Download the mission from the vehicle
    cmds = vehicle.commands

    print("Mission waypoints:")
    for cmd in cmds:
        print(cmd)

# Example usage
try:
    # Check if the vehicle is in AUTO mode
    if vehicle.mode.name == "AUTO":
        # Print the mission waypoints
        print_mission()
    else:
        print("Vehicle is not in AUTO mode.")

    # Wait for a few seconds (optional)
    time.sleep(5)

finally:
    # Close vehicle object before exiting script
    vehicle.close()
    print("Completed")
