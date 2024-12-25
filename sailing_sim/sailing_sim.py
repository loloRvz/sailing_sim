import math
import asyncio
import time

from boat import Boat
from wind import Wind
from gui import GUI

import config as cfg

async def simulation_loop(gui, boat, wind, stop_event):
    while not stop_event.is_set():
        # Check user input
        gui.check_inputs(boat)

        # Compute one physics loop
        boat.loop()

        await asyncio.sleep(cfg.TIME_STEP)

async def render_loop(gui, boat, wind, stop_event):
    cpu_load = 0
    fps = 0
    while not stop_event.is_set():
        start_time = time.time()

        # Check if game running
        if not gui.check_running():
            stop_event.set()
            break

        # Draw everything
        gui.draw(boat, wind, fps, cpu_load)


        elapsed_time = time.time() - start_time
        await asyncio.sleep(max(0, 1 / cfg.MAX_FPS - elapsed_time))

        fps = 1/(time.time() - start_time)
        cpu_load = elapsed_time * cfg.MAX_FPS

async def main():
    boat = Boat(
        init_pos = [0,0], 
        dt = cfg.TIME_STEP
    )

    wind = Wind(
        direction = -math.pi, 
        speed = 10, 
        window_width = cfg.WINDOW_WIDTH, 
        window_height = cfg.WINDOW_HEIGHT, 
        grid_size = cfg.WIND_GRID_SIZE
    )

    gui = GUI(
        width = cfg.WINDOW_WIDTH, 
        height = cfg.WINDOW_HEIGHT,
        pixel_per_meter = cfg.PIXEL_PER_METER,
        bg_colour = cfg.BLUE,
        caption = cfg.CAPTION
    )

    stop_event = asyncio.Event()

    await asyncio.gather(
        simulation_loop(gui, boat, wind, stop_event),
        render_loop(gui, boat, wind, stop_event)
    )

if __name__ == "__main__":
    asyncio.run(main())
