# Built-In
import asyncio

# External Imports
from pygame.locals import *

# Internal Imports
from core import Application
from scenes import *

def start_game():
    # Init Game & Scenes
    game = Application((320, 180), flags=FULLSCREEN | SCALED)
    game.add_scene(Title, "title")
    game.add_scene(Stream, "stream")

    # Set Current Scene
    game.set_scene("stream") # Change this to "title" in final build

    # Start Game
    asyncio.run(game.start())

# Entry Point to the program
if __name__ == "__main__":
    start_game()