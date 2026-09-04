# External Imports
import pygame
from pygame.locals import *

# Internal Imports
from core import Scene
from systems import Chat, Game, Player

# Stream Scene Class
class Stream(Scene):
    def __init__(self, scene_manager):
        super().__init__(scene_manager)

        self.background = pygame.image.load("assets/speckled-background.png")
        self.background = pygame.transform.gaussian_blur(self.background, 2)

        self.light_color = "#880088"
        self.dark_color = "#111111"

        self.chat = Chat(
            257,
            3,
            self.light_color,
            self.dark_color,
            "assets/chat-frame.png"
        )

        self.game = Game(
            3,
            3,
            self.light_color,
            self.dark_color,
            "assets/game-frame.png"
        )

        self.player = Player()

    def start(self) -> None:
        pass

    def handle_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self, delta_time: float) -> None:
        pass

    def draw(self, surface: pygame.surface.Surface) -> None:
        surface.blit(self.background)
        surface.fill(self.light_color, special_flags=pygame.BLEND_RGB_MULT)

        self.chat.draw(surface)
        self.game.draw(surface)

    def stop(self) -> None:
        pass