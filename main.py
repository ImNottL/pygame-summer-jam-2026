# Built-In
import asyncio

# Internal Imports
from core import Application
from scenes import *

# Game Class
class Game(Application):
    def __init__(self, screen_size: tuple[int, int], flags: int = 0, fps: int = 0):
        super().__init__(screen_size, flags, fps)

def start_game():
    # Init Game & Scenes
    game = Game((1920, 1080))
    game.add_scene(Title, "title")

    # Set Current Scene
    game.set_scene("title")

    # Start Game
    asyncio.run(game.start())

# Entry Point to the program
if __name__ == "__main__":
    start_game()