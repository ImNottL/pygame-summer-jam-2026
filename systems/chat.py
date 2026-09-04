# External Imports
import pygame
from pygame.locals import *

# Internal Imports
from systems import Window

class Chat(Window):
    def __init__(self, x, y, light_color, dark_color, frame_path):
        super().__init__(x, y, light_color, dark_color, frame_path)