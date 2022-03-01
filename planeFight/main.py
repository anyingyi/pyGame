import pygame
import sys
from plane import Plane,Enemy,Bullet


class Game():
    def __init__(self):
        pygame.init()

        self.size=(480,600)
        self.screen=pygame.display.set_mode(self.size)
        self.title=pygame.display.set_caption('plane fight')
        self.font=pygame.font.SysFont('Arial',30)

        # load image
        self.bg=pygame.image.load('images/background.png')
        self.bg=pygame.transform.scale(self.bg,self.size)

        self.gameover_img=pygame.image.load('images/gameover.png')

        self.height=0
        self.enemies=[]
        self.bullets=[]
        self.score=0

        self.UP=1
        self.DOWN=2
        self.LEFT=3
        self.RIGHT=4


    def draw_bg(self):
        self.height+=1
        if self.height>self.size[1]:
            self.height=0
        self.screen.blit(self.bg,(0,self.height))
        self.screen.blit(self.bg,(0,-self.size[1]+self.height))

    def creat_enemy(self,enemy_number=5):
        if len(self.enemies)>=enemy_number:
            return
        enemy=Enemy()
        self.enemies.append(enemy)

    def draw_enemies(self):
        for enemy in self.enemies:
            enemy.update(2)
            if enemy.position[1]>self.size[1] or enemy.destroy:
                self.enemies.remove(enemy)
            else:
                self.screen.blit(enemy.image,enemy.position)

    def draw_plane(self,plane=None):
        if plane.destroy==False:
            self.screen.blit(plane.image,plane.position)

    def draw_bullets(self):
        for bullet in self.bullets:
            bullet.update(1)
            if bullet.position[1]<0 or bullet.destroy:
                self.bullets.remove(bullet)
            self.screen.blit(bullet.image,bullet.position)

    def bullet_enemy_crash(self):
        for bullet in self.bullets:
            bullet_rect=bullet.rect()
            for enemy in self.enemies:
                enemy_rect=enemy.rect()
                if enemy_rect.colliderect(bullet_rect):
                    enemy.destroy=True
                    bullet.destroy=True
                    self.score+=1

    def plane_enemy_crash(self,plane=None):
        plane_rect=plane.rect()
        for enemy in self.enemies:
            enemy_rect=enemy.rect()
            if enemy_rect.colliderect(plane_rect):
                enemy.destroy=True
                plane.destroy=True

    def show_score(self):
        score=self.font.render('score:{}'.format(self.score),True,(0,0,0))
        self.screen.blit(score,(self.size[0]/2,200))

    def run(self):
        plane=Plane()
        while True:
            for event in pygame.event.get():
                print(event)
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        plane.direction=self.UP
                    elif event.key==pygame.K_DOWN:
                        plane.direction=(self.DOWN)
                    elif event.key==pygame.K_LEFT:
                        plane.direction=(self.LEFT)
                    elif event.key==pygame.K_RIGHT:
                        plane.direction=(self.RIGHT)
                    elif event.key == pygame.K_SPACE:
                        bullet=Bullet(plane)
                        self.bullets.append(bullet)


            plane.update()

            self.draw_bg()
            self.draw_plane(plane)
            self.creat_enemy()
            self.draw_enemies()
            self.draw_bullets()

            self.bullet_enemy_crash()
            self.plane_enemy_crash(plane)
            pygame.display.update()

            if plane.destroy:
                self.screen.blit(self.gameover_img,(self.size[0]/2,self.size[1]/2))
                break

            self.show_score()


if __name__ == '__main__':
    game=Game()
    game.run()
