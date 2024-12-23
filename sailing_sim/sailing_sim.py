import sys
import os

from boat import Boat
from gui import GUI

# Main loop
def main():

    boat = Boat(init_pos = [0,0], dt = 0.01)

    gui = GUI(width = 800, height = 600, caption = "Sailing Simulator")

    running = True
    while running:

        # Check if game running
        running = gui.check_running()

        # Check user input
        gui.check_inputs(boat)

        # Compute one physics loop
        boat.loop()

        # Draw everything
        gui.draw(boat)


if __name__ == "__main__":
    main()
