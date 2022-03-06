import pygame
from .. import demarrer
class Transition:
    def __init__(self):
    
        self.finished = False
        self.next ='niveau'
        self.tr = demarrer.GRAPHICS['transition']
        self.tr_rect=self.tr.get_rect()# 让图片变成矩形
        self.tr=pygame.transform.scale(self.tr,(int(self.tr_rect.width*0.51),int(self.tr_rect.height*0.49)))
        self.viewport=demarrer.SCREEN.get_rect()
        self.timer=0
    def update(self,surface,keys):
        self.draw(surface)
        if self.timer==0:
            self.timer =pygame.time.get_ticks()
        elif pygame.time.get_ticks() - self.timer>2000:
            self.finished=True
            self.timer=0
    def draw(self,surface):
        surface.blit(self.tr,(0,0))