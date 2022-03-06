import pygame
from.. import constants as C
pygame.font.init()

class Info:
    def __init__(self,state):
        self.state=state
        self.create_state_labels()
        