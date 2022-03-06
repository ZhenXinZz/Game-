import pygame
from .. import demarrer
from .. import tools

class MainMenu:
    def __init__(self):
        self.setup_background()#设置底图
        self.setup_player()#设置玩家
        self.setup_cursor()#设置光标
        self.finished=False
        self.next='transition'
        
    def setup_background(self):
        self.background = demarrer.GRAPHICS['bg'] # 利用已经存在demarrer里面的变量直接抠图
        self.background_rect=self.background.get_rect()# 让图片变成矩形
        self.viewport=demarrer.SCREEN.get_rect()
        self.start = demarrer.GRAPHICS['开始游戏']
        self.background=pygame.transform.scale(self.background,(int(self.background_rect.width*0.68)
                                                        ,int(self.background_rect.height*0.67)))
        self.start_rect=self.background.get_rect()
        
        
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

        surface.blit(self.background,self.viewport)
        surface.blit(self.start,(274,227))
        surface.blit(self.cursor.image,self.cursor.rect)
        