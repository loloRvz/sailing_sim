# GUI
PIXEL_PER_METER = 10    # [1/m] Pixels per meter
WINDOW_WIDTH = 800      # []Window width
WINDOW_HEIGHT = 600
W_HALF = WINDOW_WIDTH / PIXEL_PER_METER / 2
H_HALF = WINDOW_HEIGHT / PIXEL_PER_METER / 2
CAPTION = "Sailing Simulator"

# Simulation
MAX_FPS = 3000          # [Hz] Max FPS
TIME_STEP = 0.01        # [s] Time step

# Boat
BOAT_M = 20             # [kg] Mass
BOAT_J = 40             # [kg*m^2] Moment of inertia

BOAT_b = 10             # [N*s/m] Linear damping
BOAT_v = 40             # [] Angular damping

BOAT_F = 1000           # [N] Motor force
BOAT_R = 30             # [N*s] Rudder force per longitudinal velocity
BOAT_K = 100            # [N*s/m] Keel force per lateral velocity

BOAT_shape =[
    [3,0],
    [2,-1],
    [-3,-1],
    [-3,1],
    [2,1]]              # [m] Boat shape

# Wind
WIND_GRID_SIZE = 2      # [m] Wind grid size

# Colors
BLUE = (70, 130, 180)   # Water color
WHITE = (255, 255, 255)
