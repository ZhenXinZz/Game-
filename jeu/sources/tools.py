import pygame
import os

#1.初始化界面

class Game:
    def __init__(self,state_dict,start_state):  # 游戏初始化(initialisation du jeu)
        pygame.init()
        pygame.display.set_mode((1300,700))
        pygame.display.set_caption('Nian')
        icon=pygame.image.load(os.path.join('ressources','imageetsprite','icon.jpg'))
        pygame.display.set_icon(icon)
        self.start=pygame.image.load(os.path.join('ressources','imageetsprite','开始游戏.png'))
        self.screen=pygame.display.get_surface()
        self.clock = pygame.time.Clock()# fps 游戏帧数和\
        self.keys=pygame.key.get_pressed()
        self.state_dict=state_dict
        self.state=self.state_dict[start_state]
        
    def update(self):
        if self.state.finished:
            next_state=self.state.next
            self.state.finished=False
            self.state=self.state_dict[next_state]
        self.state.update(self.screen,self.keys)
            
                               
#游戏主循环
    def run(self):
        running=True
        while running :
            #self.screen.blit(self.bg,(0,0)) # 用于显示照片，而00 则为照片显示的位置
            #self.screen.blit(self.start,(274,227))
            for event in pygame.event.get():  #pygame 所收到的指令
                if event.type== pygame.QUIT:
                    running=False
                elif event.type== pygame.KEYDOWN:
                    self.keys=pygame.key.get_pressed()#现在keys为0 和 1组成的列表 他会根据按键而变化
                elif event.type== pygame.KEYUP:
                    self.keys=pygame.key.get_pressed() 
            
            #if keys[pygame.K_DOWN]:
                    #人物.rect.y+=10
                #if keys[pygame.K_UP]:
                       #人物.rect
            #image=get_image(GRAPHICS['run'], 1, 1,65, 50, (255,255,255), 1)
            #self.screen.blit(image,(100,100))
            #state.update(self.screen,self.keys)
            self.update()
            pygame.display.update()# 用于每次更新页面
            self.clock.tick(30)
        pygame.quit()


#用于截取图片 简称抠图
def load_graphics(path,accept=('.jpg','.png','.bap','.gif')): # 加载图片的函数，而这个函数只接受两个函数 , path = 存放图片的文件夹, accecpt= 接受的格式 
    graphics={}
    for pic in os.listdir(path):
        name,ext= os.path.splitext(pic) # 拆分文件, 文件名 + 后缀( extention)
        if ext.lower() in accept:
            img=pygame.image.load(os.path.join(path,pic))# 载入图片 
            if img.get_alpha(): #alpha 层 = 透明底 
                img=img.convert_alpha() #  改成透明层的格式 
            else:
                img=img.convert()
            graphics[name]=img
    return graphics

def get_image(sheet,x,y,width,height,colorkey,scale):# sheet 传入一张图片 
    image=pygame.Surface((width,height))
    image.blit(sheet,(0,0),(x,y,width,height))# 0,0 代表画到哪里, x,y,w,h dai biao 
    image.set_colorkey(colorkey)
    image=pygame.transform.scale(image,(int(width*scale),int(height*scale)))# 扩大图片，scale为扩大的倍数
    return image 
