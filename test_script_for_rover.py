from dronekit import connect
from dronekit import VehicleMode 
import time 

# Connect to UDP endpoint.
vehicle = connect("tcp:127.0.0.1:5762", wait_ready=True)
# Use returned Vehicle object to query device state - e.g. to get the mode:
print("Mode: %s" % vehicle.mode.name)

vehicle.mode = VehicleMode( 'GUIDED' )

time.sleep(2)

print("Mode: %s" % vehicle.mode.name)
