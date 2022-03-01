import pygame
import sys

pygame.init()
screen=pygame.display.set_mode((500,500))
title=pygame.display.set_caption('hello world')

ball_x=250
ball_y=250

# load image
pic=pygame.image.load('ship.bmp')
pic=pygame.transform.scale(pic,(50,50))
#screen.blit(pic,(0,0))

# load words
myfont=pygame.font.SysFont('arial',50)
words=myfont.render('你好,pygame!',True,'white')
screen.blit(words,(250,250))

while True:
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                ball_x-=5
            elif event.key==pygame.K_RIGHT:
                ball_x+=5
        elif event.type==pygame.MOUSEMOTION:
            xy=pygame.mouse.get_pos()
            ball_x=xy[0]
            ball_y=xy[1]
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                pic=pygame.transform.rotate(pic,90)
            elif event.button==3:
                pic=pygame.transform.rotate(pic,-90)

    screen.fill('black')
    screen.blit(words, (250, 250))
    screen.blit(pic, (ball_x, ball_y))
    pygame.display.update()
