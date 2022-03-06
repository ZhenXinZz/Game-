import pygame
from .. import demarrer
from.. comportement import player,stuff
import json
import os 
class Niveau:
    def __init__(self):
        self.finished = False
        self.next =None
        self.setup_background()
        self.load_map_data()        
        self.setup_start_position()
        self.setup_player()
        self.setup_ground_items()

        
    def load_map_data(self):
        file_name='map1.json'
        file_path=os.path.join('sources/data/maps',file_name)
        with open(file_path) as f:
            self.map_data = json.load(f)
        
     
    def setup_start_position(self):
        self.position=[]
        for data in self.map_data['map']:
            self.position.append((data['start_x'],data['end_x'],data['player_x'],data['player_y']))
        self.start_x,self.end_x,self.player_x,self.player_y =self.position[0]
     
    def setup_background(self):
        self.map = demarrer.GRAPHICS['map'] # 利用已经存在demarrer里面的变量直接抠图
        rect=self.map.get_rect()# 让图片变成矩形
        self.map=pygame.transform.scale(self.map,(int(rect.width*1.5),
                                                    int(rect.height*0.51)))
        self.map_rect=self.map.get_rect()# 让图片变成矩形
        self.game_window=demarrer.SCREEN.get_rect()
        self.game_ground = pygame.Surface((self.map_rect.width, self.map_rect.height))
        

    
    def setup_player(self):
        self.player=player.Player('er2')
        self.player.rect.x=self.game_window.x + self.player_x
        self.player.rect.bottom=self.player_y
    
    
    
    def setup_ground_items(self):
        self.ground_items_group = pygame.sprite.Group()
        for name in ['sol']:
            for item in self.map_data[name]:
                self.ground_items_group.add(stuff.Item(item['x'],item['y'],item['width'],item['height'],name))
    
    
    
    def update(self,surface,keys):
        self.player.update(keys)
        self.update_player_position()
        self.update_game_window()
        self.draw(surface)
        

    def update_player_position(self):
        self.player.rect.x+= self.player.x_vel
        if self.player.rect.x< self.start_x:
            self.player.rect.x=self.start_x
        elif self.player.rect.right > self.end_x:
            self.player.rect.right = self.end_x
        self.check_x_collisions()
        self.player.rect.y+= self.player.y_vel
        self.check_y_collisions()


    def check_x_collisions(self):
        ground_item = pygame.sprite.spritecollideany(self.player,self.ground_items_group)
        if ground_item:
            self.adjust_player_x(ground_item)
            
            
    def check_y_collisions(self):
        ground_item = pygame.sprite.spritecollideany(self.player,self.ground_items_group)
        if ground_item:
            self.adjust_player_y(ground_item)
        self.check_will_fall(self.player)
            
    def adjust_player_x (self,sprite):
        if self.player.rect.x < sprite.rect.x:
            self.player.rect.right = sprite.rect.left
        else:
            self.player.rect.left=sprite.rect.right
        self.player.x_vel = 0
        
        
    def adjust_player_y (self,sprite):
        if self.player.rect.bottom < sprite.rect.bottom:
           self.player.y_vel=0
           self.player.rect.bottom = sprite.rect.top
           self.player.state = 'stand'
        else:
            self.player.y_vel = 7
            self.player.rect.top=sprite.rect.bottom
            self.player.state = 'fall'

    def check_will_fall(self,sprite):
        sprite.rect.y+=1
        check_group = pygame.sprite.Group(self.ground_items_group)
        collided = pygame.sprite.spritecollideany(sprite,check_group)
        if not collided and sprite.state!= 'jump' :
            sprite.state = 'fall'
        sprite.rect.y -=1
        
    def update_game_window(self):
        tier = self.game_window.x + self.game_window.width/3
        if self.player.x_vel > 0 and self.player.rect.centerx > tier and self.game_window.right< self.end_x:
            self.game_window.x+= self.player.x_vel
            self.start_x = self.game_window.x
        

    def draw(self,surface):
        self.game_ground.blit(self.map,self.game_window,self.game_window)
        self.game_ground.blit(self.player.image,self.player.rect)
        surface.blit(self.game_ground,(0,0),self.game_window)
        
        