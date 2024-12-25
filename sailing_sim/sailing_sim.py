import math
import asyncio

from boat import Boat
from wind import Wind
from gui import GUI

from config import WINDOW_WIDTH, WINDOW_HEIGHT, PIXEL_PER_METER, CAPTION, MAX_FPS, WIND_GRID_SIZE, TIME_STEP

async def simulation_loop(gui, boat, wind, stop_event):
    while not stop_event.is_set():
        # Check user input
        gui.check_inputs(boat)

        # Compute one physics loop
        boat.loop()

        await asyncio.sleep(TIME_STEP)

async def render_loop(gui, boat, wind, stop_event):
    while not stop_event.is_set():
        # Check if game running
        if not gui.check_running():
            stop_event.set()
            break

        # Draw everything
        gui.draw(boat, wind)

        await asyncio.sleep(1 / MAX_FPS)

async def main():
    boat = Boat(
        init_pos = [0,0], 
        dt = TIME_STEP)

    wind = Wind(
        direction = -math.pi, 
        speed = 10, 
        window_width = WINDOW_WIDTH, 
        window_height = WINDOW_HEIGHT, 
        grid_size = WIND_GRID_SIZE)

    gui = GUI(
        width = WINDOW_WIDTH, 
        height = WINDOW_HEIGHT,
        pixel_per_meter = PIXEL_PER_METER,
        caption = CAPTION, 
        max_fps=MAX_FPS)

    stop_event = asyncio.Event()

    await asyncio.gather(
        simulation_loop(gui, boat, wind, stop_event),
        render_loop(gui, boat, wind, stop_event)
    )

if __name__ == "__main__":
    asyncio.run(main())
