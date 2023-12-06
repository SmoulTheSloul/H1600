from dronekit import connect, VehicleMode
import time

# Connect to the Vehicle
vehicle = connect('/dev/ttyUSB0', baud=921600, wait_ready=True)

# Function to print all mission waypoints
def print_all_waypoints():
    # Download the mission from the vehicle
    cmds = vehicle.commands

    print("Mission waypoints:")
    for i, cmd in enumerate(cmds):
        print(f"Waypoint {i+1}:")
        print(f"  Command: {cmd.command}")
        print(f"  Frame: {cmd.frame}")
        print(f"  Params: {cmd.params}")
        print(f"  Auto Continue: {cmd.autocontinue}")
        print("")

# Example usage
try:
    # Check if the vehicle is in AUTO mode
    if vehicle.mode.name == "AUTO":
        # Print all mission waypoints
        print_all_waypoints()
    else:
        print("Vehicle is not in AUTO mode.")

    # Wait for a few seconds (optional)
    time.sleep(5)

finally:
    # Close vehicle object before exiting script
    vehicle.close()
    print("Completed")
