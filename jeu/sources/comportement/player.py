import pygame
from.. import tools,demarrer 
from .. import constant as C
import json
import os
import time 


class Player(pygame.sprite.Sprite):
    def __init__(self,name):
        pygame.sprite.Sprite.__init__(self)
        self.name=name
        self.load_data()
        self.setup_states()
        self.setup_velocities()
        self.setup_timers()
        self.load_images()
        self.attack_index=9
        self.frame_index=0
        self.image= self.frames[self.frame_index]
        self.rect =self.image.get_rect()
        
    def load_data(self):
        file_name = self.name + '.json'
        file_path= os.path.join('sources/data/player',file_name)
        with open(file_path)as f:
            self.player_data = json.load(f)  #importer ;e dossier json et transformer en dictionnaire 
     
    def setup_states(self):# les etats du personnage: mort , vers droit, vers gauche 
        self.state='stand'
        self.face_right=True
        self.dead= False
        self.big= False
        self.can_jump = True
        
    def setup_velocities(self): #les donnees de la vitesse
        speed =self.player_data['speed'] # prend les valeurs de player_data avec le cle = speed
        self.x_vel=0 #vitesse initiale
        self.y_vel=0
        
        self.max_walk_vel=speed['max_walk_speed']
        self.max_run_vel=speed['max_run_speed']
        self.max_y_vel=speed['max_y_velocity']
        self.jump_vel=speed['jump_velocity']
        self.walk_accel=speed['walk_accel']
        self.run_accel=speed['run_accel']
        self.turn_accel=speed['turn_accel']
        self.gravity=C.GRAVITY
        self.anti_gravity=C.ANTI_GRAVITY
        
        self.max_x_vel =self.max_walk_vel
        self.x_accel=self.walk_accel
        
    def setup_timers(self): #chronometrer
        self.walking_timer=0
        self.timer=0
        self.transition_timer=0 
        
    def load_images(self):
        sheet=demarrer.GRAPHICS['er2']
        frame_rects = self.player_data['image_frames']
        
        self.right_normal_frames=[]
        self.left_normal_frames=[]
        
        self.normal_frames= [self.right_normal_frames,self.left_normal_frames]
        
        
        self.all_frames= [
            self.right_normal_frames,
            self.left_normal_frames,
            ]
        
        
        self.right_frames= self.right_normal_frames
        self.left_frames= self.left_normal_frames
        
        
        for group,group_frame_rects in frame_rects.items():        
            for frame_rect in group_frame_rects:
                right_image= tools.get_image(sheet,frame_rect['x'],frame_rect['y'],frame_rect['width'],frame_rect['height'],(0,135,0),0.8)
                left_image = pygame.transform.flip(right_image,True,False)
                if group== 'right_normal':
                    self.right_normal_frames.append(right_image)
                    self.left_normal_frames.append(left_image)
        #self.frames.append(tools.get_image(sheet,9,4,61,46,(0,0,0),1))
        
        self.frame_index=0
        self.frames=self.right_frames
        self.image=self.frames[self.frame_index]
        self.rect=self.image.get_rect()
        
    def update(self,keys):
        self.current_time = pygame.time.get_ticks()
        self.handle_states(keys)
    
    
    def handle_states(self,keys):
        self.can_jump_or_not(keys)
        
        
        if self.state == 'stand':
            self.stand(keys)
        elif self.state=='run':
            self.run(keys)
        elif self.state=='jump':
            self.jump(keys)
        elif self.state == 'fall':
            self.fall(keys)
        elif self.state == 'attack':
            for i in range(4):
                self.attack(keys)
        if self.face_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image= self.left_frames[self.frame_index]
        
    def stand(self,keys):
        self.frame_index = 7
        self.x_vel=0
        self.y_vel=0
            
        if keys[pygame.K_d]:
            self.face_right = True
            self.state = 'run'
        elif keys[pygame.K_a]:
            self.face_right = False
            self.state = 'run'
        elif keys[pygame.K_k] and self.can_jump: 
            self.state = 'jump'
            self.y_vel = self.jump_vel
        elif keys[pygame.K_j]:
            self.state = 'attack'
    def run(self,keys):
        self.max_x_vel = self.max_walk_vel
        self.x_accel = self.run_accel
        self.x_vel=0
        
        if self.current_time - self.walking_timer >100:
            self.walking_timer =self.current_time
            self.frame_index+=1
            self.frame_index%=6
        if keys[pygame.K_d]:
            self.face_right= True
            #if self.x_vel<0:
                #self.frame= self.left_frames
                #self.x_accel = self.turn_accel
                #self.x_vel = self.calc_vel(self.x_vel,self.x_accel, self.max_x_vel, True)
            self.x_vel=4.5
        if keys[pygame.K_d] and keys[pygame.K_SPACE]:
            self.face_right =True
            self.x_vel = 6.5
        if keys[pygame.K_a]:
            self.face_right = False
            #if self.x_vel > 0:
                #self.frame = self.right_frames
                #self.x_accel = self.turn_accel
            #self.x_vel = self.calc_vel(self.x_vel,self.x_accel, self.max_x_vel, False)
            self.x_vel=-4.5
        if keys[pygame.K_a] and keys[pygame.K_SPACE]:
             self.face_right =False
             self.x_vel=-6.5
        if self.x_vel == 0:
            self.state='stand'
        if keys[pygame.K_k] and self.can_jump:
            self.state='jump'
            self.y_vel = self.jump_vel
        if keys[pygame.K_j]:
            self.state = 'attack'
    def jump(self,keys):
        self.frame_index= 6
        self.y_vel += self.anti_gravity
                
        self.can_jump = False
        if self.y_vel >= 0:
            self.state = 'fall'
        if keys[pygame.K_d]:
            self.x_vel = self.calc_vel(self.x_vel,self.x_accel, self.max_x_vel, True)
            self.face_right =True
        elif keys[pygame.K_a]:
            self.x_vel = self.calc_vel(self.x_vel,self.x_accel, self.max_x_vel, False)
            self.face_right=False
    
    def fall(self,keys):
        self.y_vel = self.calc_vel (self.y_vel,self.gravity,self.max_y_vel)
        self.frame_index =8
        if keys[pygame.K_d]:
            self.x_vel = self.calc_vel(self.x_vel,self.x_accel, self.max_x_vel, True)
            self.face_right =True
        if keys[pygame.K_a]:
            self.x_vel = self.calc_vel(self.x_vel,self.x_accel, self.max_x_vel, False)
            self.face_right=False
    
    def attack(self,keys):
        self.frame_index=9
        self.frame_index=10

                

                        
                
            
            
            
        self.state = 'stand'
        
                
            
    
    def can_jump_or_not(self,keys):
        if not keys[pygame.K_k]:
            self.can_jump = True
        


            
        
    
    def calc_vel(self,vel,accel,max_vel,is_positive= True):
        if is_positive:
            return min(vel + accel ,max_vel)
        else:
            return max(vel - accel,-max_vel)
        
        
        
