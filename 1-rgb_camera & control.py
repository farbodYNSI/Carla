import carla
import random
import cv2
import numpy as np

# RGB camera image variable
raw_image = 0

# Connect to Carla
client = carla.Client('localhost', 2000)
world = client.get_world()

# Get a vehicle from the library
bp_lib = world.get_blueprint_library()
vehicle_bp = bp_lib.find('vehicle.lincoln.mkz_2020')

# Get a spawn point
spawn_points = world.get_map().get_spawn_points()

# Spawn a vehicle
vehicle = world.try_spawn_actor(vehicle_bp, random.choice(spawn_points))

# Autopilot
vehicle.set_autopilot(True) 

# Get the world spectator 
spectator = world.get_spectator() 

## Part 2

# Create a camera floating behind the vehicle
camera_init_trans = carla.Transform(carla.Location(x=0.75, z=2.5), carla.Rotation(pitch=-10))

# Create a RGB camera
rgb_camera_bp = world.get_blueprint_library().find('sensor.camera.rgb')
camera = world.spawn_actor(rgb_camera_bp, camera_init_trans, attach_to=vehicle)

# Define a callback function to process camera frames
def process_image(image):
    global raw_image
    array = np.frombuffer(image.raw_data, dtype=np.uint8)
    array = array.reshape((image.height, image.width, 4))
    array = array[:, :, :3]  # Remove the alpha channel
    raw_image = array

# Start listening to the camera sensor
camera.listen(lambda image: process_image(image))

# OpenCV named window for rendering
cv2.namedWindow('RGB Camera', cv2.WINDOW_AUTOSIZE)

# Clear the spawned vehicle and camera
def clear():

    vehicle.destroy()
    print('Vehicle Destroyed.')
    
    camera.stop()
    camera.destroy()
    print('Camera Destroyed. Bye!')

    for actor in world.get_actors().filter('*vehicle*'):
        actor.destroy()

    cv2.destroyAllWindows()

# Main loop
while True:
    try:
        # Move the spectator to the top of the vehicle 
        transform = carla.Transform(vehicle.get_transform().transform(carla.Location(x=-4,z=50)), carla.Rotation(yaw=-180, pitch=-90)) 
        spectator.set_transform(transform) 
        
        # Control the speed and steering
        control = carla.VehicleControl()
        control.throttle = 1.0
        control.brake = 1.0
        control.steer = -1.0  # Steer left
        control.steer = 1.0   # Steer right
        control.hand_brake = True
        vehicle.apply_control(control)

        # Display RGB camera image
        cv2.imshow('RGB Camera', raw_image)
        # Quit if user presses 'q'
        if cv2.waitKey(1) == ord('q'):
            clear()
            break

    except KeyboardInterrupt as e:
        clear()
        break
