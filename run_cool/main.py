import pygame as pg
import sys
import numpy as np
import time


class Man():
    def __init__(self):
        self.bili = pg.image.load('yiyang.png')
        self.img = pg.transform.scale(self.bili, (60, 85))
        self.man_pos = [200, 415]
        self.gravity = 0.2
        self.man_vy = 0
        self.onfloor=True

    def update(self):
        self.man_vy+=self.gravity
        self.man_pos[1]+=self.man_vy
        if self.man_pos[1]>=415:
            self.man_vy=0
            self.man_pos[1]=415
            self.onfloor = True

    def rect(self):
        rectangle=self.img.get_rect()
        rectangle.left,rectangle.top=self.man_pos
        return rectangle


class Obstacle():
    def __init__(self):
        self.img = pg.Surface((30, 200))
        self.img.fill('white')
        self.pos = [600, 410]

    def update(self):
        self.pos[0] -= 2
        if self.pos[0] < 0:
            self.pos[1] = np.random.randint(350, 450)
            self.pos[0] = 850

    def rect(self):
        rectangle = self.img.get_rect()
        rectangle.left, rectangle.top = self.pos
        return rectangle


class Game():
    def __init__(self):
        pg.init()

        self.screen=pg.display.set_mode((800,500))
        pg.display.set_caption('runcool')

        self.font=pg.font.Font(None,50)
        self.coin=0
        self.passed=True

        self.man=Man()
        self.piece=Obstacle()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_SPACE and self.man.onfloor:
                        self.man.man_vy=-10
                        self.man.onfloor=False

            self.screen.fill((0,0,0))
            self.screen.blit(self.man.img,self.man.man_pos)
            self.screen.blit(self.piece.img, self.piece.pos)
            self.show_coin()

            self.man.update()
            self.piece.update()
            self.man_piece_crash()
            self.get_coin()

            pg.display.update()
            time.sleep(0.01)

    def show_coin(self):
        coin = self.font.render('coin:{}'.format(self.coin), True, (255, 0, 0))
        self.screen.blit(coin, (20, 20))

    def get_coin(self):
        if self.piece.pos[0]<=0:
            self.passed=True
        if self.passed and self.man.man_pos[0]>self.piece.pos[0]:
            self.coin+=1
            self.passed=False

    def man_piece_crash(self):
        man_rect = self.man.rect()
        piece_rect = self.piece.rect()
        if man_rect.colliderect(piece_rect):
            print('coins:{}'.format(self.coin))
            pg.quit()
            sys.exit()


if __name__ == '__main__':
    game=Game()
    game.run()

