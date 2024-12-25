# GUI
PIXEL_PER_METER = 10    # [1/m] Pixels per meter
WINDOW_WIDTH = 800      # []Window width
WINDOW_HEIGHT = 600
W_HALF = WINDOW_WIDTH / PIXEL_PER_METER / 2
H_HALF = WINDOW_HEIGHT / PIXEL_PER_METER / 2
CAPTION = "Sailing Simulator"
PRINT_PERF = False      # Print performance data

# Simulation
MAX_FPS = 60            # [Hz] Max FPS
TIME_STEP = 0.01        # [s] Time step

# Boat
BOAT_M = 500            # [kg] Mass
BOAT_J = 400            # [kg*m^2] Moment of inertia
BOAT_b = 50             # [N*s/m] Linear damping
BOAT_v = 100            # [] Angular damping
BOAT_F = 500            # [N] Motor force
BOAT_R = 30             # [N*s] Rudder force per longitudinal velocity
BOAT_K = 300            # [N*s/m] Keel force per lateral velocity

BOAT_shape = [
    [  -3,  0.7],       # stern portside
    [-1.5,    1],
    [ 0.5,    1],
    [ 2.2,  0.5],
    [   3,    0],       # bow
    [ 2.2, -0.5],
    [ 0.5,   -1],
    [-1.5,   -1],
    [  -3, -0.7],       # stern starboard
]                       # [m] Boat shape

# Wind
WIND_GRID_SIZE = 2      # [m] Wind grid size

# Colors
BLUE = (70, 130, 180)   # Water color
WHITE = (255, 255, 255)
