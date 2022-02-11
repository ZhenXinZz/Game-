import pygame
from .. import demarrer
class Transition:
    def __init__(self):
    
        self.finished = False
        self.next ='niveau'
        self.tr = demarrer.GRAPHICS['transition'] 
        self.tr_rect=self.tr.get_rect()# 让图片变成矩形
        self.viewport=demarrer.SCREEN.get_rect()
    def update(self,surface,keys):
        self.draw(surface)

    def draw(self,surface):
        surface.blit(self.tr,self.viewport)
        