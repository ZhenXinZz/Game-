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
        self.start=pygame.image.load(r'C:\Thonny\jeu\ressources\imageetsprite\开始游戏.png')
        self.screen=pygame.display.get_surface()
        self.clock = pygame.time.Clock()# fps \
        self.keys=pygame.key.get_pressed()
        self.state_dict=state_dict
        self.state=self.state_dict[start_state]#depend les etapes du jeu 
        
    def update(self):
        if self.state.finished:
            next_state=self.state.next# prochaine etape
            self.state.finished=False
            self.state=self.state_dict[next_state] #aller sur le prochain étape
        self.state.update(self.screen,self.keys)
            
                               
#游戏主循环
    def run(self):
        running=True
        while running :
            for event in pygame.event.get():  #pygame les commandes ou les evenement recus
                if event.type== pygame.QUIT:
                    running=False
                elif event.type== pygame.KEYDOWN:
                    self.keys=pygame.key.get_pressed()#现在keys为0 和 1组成的列表 他会根据按键而变化, keys est construit par une liste de 0 et 1 , donc chaque key est definit par la liste 
                elif event.type== pygame.KEYUP:
                    self.keys=pygame.key.get_pressed() 
            self.update()
            pygame.display.update()# pour charger/mise à jour le programme
            self.clock.tick(30)#fps
        pygame.quit()


#用于截取图片 简称抠图
def load_graphics(path,accept=('.jpg','.png','.bap','.gif')): # 加载图片的函数，而这个函数只接受两个函数 , path = le chemin pour acceder l'image, accecpt= format acceptée 
    graphics={}
    for pic in os.listdir(path):
        name,ext= os.path.splitext(pic) # separer le nom du fichier, nom + 后缀( extention)
        if ext.lower() in accept:
            img=pygame.image.load(os.path.join(path,pic))# importer l'image
            if img.get_alpha(): #alpha 层 = base transparante
                img=img.convert_alpha() #  改成透明层的格式 
            else:
                img=img.convert()
            graphics[name]=img
    return graphics

def get_image(sheet,x,y,width,height,colorkey,scale):# sheet :l'endroit où se trouve une image 
    image=pygame.Surface((width,height))
    image.blit(sheet,(0,0),(x,y,width,height))# 0,0 les ordonnées où on commence à dessiner  
    image.set_colorkey(colorkey)# photoshoper
    image=pygame.transform.scale(image,(int(width*scale),int(height*scale)))# redimentionner l'image，scale : coefficient
    return image 
