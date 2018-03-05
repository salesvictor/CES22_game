import pygame

from models.Ship import Ship
from ui.TextBox import TextBox
from ui.LivesBar import LivesBar


class Player:
    INITIAL_LIVES = 3
    MAX_LIVES = 5
    NAME_BOX_FONT_SIZE = 20
    SCORE_BOX_FONT_SIZE = 20

    def __init__(self, screen, x, y, number):
        self.lives = self.INITIAL_LIVES
        self.score = 0
        self.number = number
        self.name = "PLAYER{}".format(number)
        self.screen = screen

        # Calculate position of text boxes and lives bar
        self.display_width_factor = screen.get_width() / 800
        self.display_height_factor = screen.get_height() / 640
        self.NAME_BOX_CENTER = (self.display_width_factor * 100, self.display_height_factor * 25)
        self.SCORE_BOX_CENTER = (self.display_width_factor * 100, self.display_height_factor * 50)
        self.LIVES_BAR_CENTER = (self.display_width_factor * 100, self.display_height_factor * 80)

        # Create text boxes and lives bar
        self.name_box = TextBox(self.NAME_BOX_CENTER, self.NAME_BOX_FONT_SIZE, self.name)
        self.score_box = TextBox(self.SCORE_BOX_CENTER, self.SCORE_BOX_FONT_SIZE, "{}".format(self.score))
        self.lives_bar = LivesBar(self.LIVES_BAR_CENTER, self.lives)

        # Create ship
        self.ship = Ship(screen, x, y)
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.ship)

    def update(self):
        self.score_box.set_dialogue("{}".format(self.score))
        self.lives_bar.set_lives(self.lives)
        self.sprites.update()

    def render(self):
        self.name_box.render(True, (255, 255, 255), self.screen)
        self.score_box.render(True, (255, 255, 255), self.screen)
        self.lives_bar.render(self.screen)
        self.sprites.draw(self.screen)