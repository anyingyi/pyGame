import pygame
import numpy as np

class Plane():
    def __init__(self):
        self.bg_size=(470,600)
        self.image_path='images/me.png'
        self.image=pygame.image.load(self.image_path)
        self.position=[self.bg_size[0]/2,self.bg_size[1]*3/4]
        self.move=1
        self.direction=None
        self.destroy=False

    def update(self):
        if self.direction==1:
            self.position[1]-=self.move
        elif self.direction==2:
            self.position[1]+=self.move
        elif self.direction==3:
            self.position[0]-=self.move
        elif self.direction==4:
            self.position[0]+=self.move

    def rect(self):
        rectangle=self.image.get_rect()
        rectangle.left,rectangle.top=self.position
        return rectangle


class Enemy():
    def __init__(self):
        self.bg_size=(470,600)
        self.image_path='images/enemy.png'
        self.image=pygame.image.load(self.image_path)
        self.position=[np.random.randint(0,self.bg_size[0]),0]
        self.move=1
        self.destroy = False

    def update(self,direction):
        if direction==1:
            self.position[1]-=self.move
        elif direction==2:
            self.position[1]+=self.move
        elif direction==3:
            self.position[0]-=self.move
        elif direction==4:
            self.position[0]+=self.move

    def rect(self):
        rectangle=self.image.get_rect()
        rectangle.left,rectangle.top=self.position
        return rectangle


class Bullet():
    def __init__(self,plane=None):
        self.bg_size=(470,600)
        self.image_path='images/bullet.png'
        self.image=pygame.image.load(self.image_path)
        self.x=plane.position[0]+plane.image.get_size()[0]/2
        self.y=plane.position[1]
        self.move=5
        self.position = [self.x,self.y]
        self.destroy = False

    def update(self,direction):
        if direction==1:
            self.position[1]-=self.move
        elif direction==2:
            self.position[1]+=self.move
        elif direction==3:
            self.position[0]-=self.move
        elif direction==4:
            self.position[0]+=self.move

    def rect(self):
        rectangle=self.image.get_rect()
        rectangle.left,rectangle.top=self.position
        return rectangle