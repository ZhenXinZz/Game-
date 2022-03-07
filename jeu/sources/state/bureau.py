import pygame
from .. import demarrer
from .. import tools

class MainMenu:
    def __init__(self):
        self.setup_background()#créer le backgroung
        self.setup_player()#créer le personnage
        self.setup_cursor()#créer le curseur
        self.finished=False
        self.next='transition'
        
    def setup_background(self):
        self.background = demarrer.GRAPHICS['bg'] 
        self.background_rect=self.background.get_rect()# transformer les images en quadrilatère
        self.viewport=demarrer.SCREEN.get_rect()
        self.start = demarrer.GRAPHICS['开始游戏']
        self.background=pygame.transform.scale(self.background,(int(self.background_rect.width*0.68)
                                                        ,int(self.background_rect.height*0.67)))

        
        
    def setup_player(self):
        pass
    
    def setup_cursor(self):
        self.cursor=pygame.sprite.Sprite()
        self.cursor.image= tools.get_image(demarrer.GRAPHICS['curser'],73,80,167,155,(255,255,255),0.1)
        rect= self.cursor.image.get_rect()
        rect.x,rect.y=(300,277)
        self.cursor.rect=rect
        self.cursor.state='start'
    def update_cursor(self,keys):
        if keys[pygame.K_UP]:
            self.cursor.state='start'
            self.cursor.rect.y=277
        elif keys[pygame.K_RETURN]:
            if self.cursor.state=='start':
                 self.finished = True #wan jie zhuang tai 
            

    def update(self,surface,keys): #更新+绘画
        
        self.update_cursor(keys)

        surface.blit(self.background,self.viewport)# self.viewport(0,0)
        surface.blit(self.start,(274,227))
        surface.blit(self.cursor.image,self.cursor.rect)
        
