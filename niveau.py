import pygame

class Niveau:
    def __init__(self):
        self.finished = False
        self.next =None
        self.map = demarrer.GRAPHICS['map'] # 利用已经存在demarrer里面的变量直接抠图
        self.map_rect=self.map.get_rect()# 让图片变成矩形
        self.viewport=demarrer.SCREEN.get_rect()
    def update(self,surface,keys):
        self.draw(suface)

    def draw(self,surface):
        surface.blit(self.map,self.viewport)
        
    