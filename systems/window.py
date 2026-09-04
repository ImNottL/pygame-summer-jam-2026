# External Imports
import pygame
from pygame.locals import *

class Window:
    def __init__(self, x, y, light_color, dark_color, frame_path):
        self.position = pygame.Vector2(x, y)
        self.light_color = light_color
        self.dark_color = dark_color

        self.frame = pygame.image.load(frame_path)
        self.frame = pygame.transform.grayscale(self.frame)
        self.frame.fill(self.light_color, special_flags=BLEND_RGB_MULT)
        
    def draw(self, surface: pygame.surface.Surface) -> None:
        pygame.draw.rect(surface, self.dark_color, (
            self.position.x, 
            self.position.y,
            self.frame.width,
            self.frame.height
        ))
        
        surface.blit(self.frame, self.position)