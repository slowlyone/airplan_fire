import pygame
from plane_sprites import *

pygame.init()
screen=pygame.display.set_mode((480,700))
bg=pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
pygame.display.update()

hero=pygame.image.load("./images/me1.png")
screen.blit(hero,(150,300))
pygame.display.update()
clock=pygame.time.Clock()
#1.定义rect记录飞机对初始位置
hero_rect=pygame.Rect(150,300,102,126)
#创建敌机精灵
enemy=GameSprite("./images/enemy1.png")
enemy1=GameSprite("./images/enemy1.png",2)
#创建敌机的精灵组
enemy_group=pygame.sprite.Group(enemy,enemy1)

while  True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print('退出游戏')
            pygame.quit()
            exit()
#    2.修改飞机位置
    hero_rect.y -= 1
#  判断飞机对位置  y值
    if hero_rect.y==-126:
        hero_rect.y=700
#    3.调用blit方法绘制图像
    screen.blit(bg,(0, 0))
    screen.blit(hero,hero_rect)   #位置可以跟一个变量

#让精灵组调用两个方法/
#update
    enemy_group.update()
#draw()
    enemy_group.draw(screen)

#    4.调用update方法更新显示
    pygame.display.update()

pygame.quit()