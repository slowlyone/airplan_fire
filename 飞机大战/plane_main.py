import pygame
from plane_sprites import *

class PlanGame(object):
    '''飞机大战主游戏'''
    def __init__(self):
        self.clock=pygame.time.Clock()
        self.screen=pygame.display.set_mode(GAME_RECT.size)
        self.__create_sprites()
        pygame.time.set_timer(GREATE_EVEM_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)

    def __create_sprites(self):

        # self.background=Background("./images/background.png")
        # self.background2 = Background("./images/background.png")
        self.background = Background()
        self.background2 = Background(is_alt=1)
        # self.background2.rect.y=-GAME_RECT.height   会偶尔卡一下屏幕～～？
        # self.background2.rect.y = -self.background2.rect.height
        self.background_group=pygame.sprite.Group(self.background,self.background2)
        self.hero=Hero()
        # self.enemy = Enemy()
        # self.enemy1 = Enemy()
        # self.enemy_group = pygame.sprite.Group(self.enemy, self.enemy1)
        self.enemy_group=pygame.sprite.Group()
        self.hero_group=pygame.sprite.Group(self.hero)
        # self.fire=Fire()
        # self.bullet_group=pygame.sprite.Group()

    def  Gamestart(self):
        while True:
            # 1.设置刷新帧率
            self.clock.tick(TIME_BIT)
            #2.事件监听
            self.__event_handler()
            #3.碰撞监测
            self.__check_collide()
            #4.更新/绘制精灵组
            self.__update_sprites()
            #5.更新显示
            pygame.display.update()


    def  __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlanGame.__game_quit()
            elif event.type == GREATE_EVEM_EVENT:
                # print("敌机出场")
                self.enemy=Enemy()
                self.enemy_group.add(self.enemy)
                # print("退出游戏")
                # pygame.quit()
                # exit()
            elif event.type == HERO_FIRE_EVENT:
                # self.bullet1=Bullet()
                # self.bullet1.rect.centerx=self.hero.rect.centerx
                # self.bullet_group.add(self.bullet1)
                self.hero.fire()
            # elif  event.type == pygame.KEYDOWN  and event.key == pygame.K_RIGHT:
            #     print("向右移动")
        #使用键盘提供对方法获取键盘按键 --按键元组
        keys_pressed =pygame.key.get_pressed()
        #判断元组中对应对按键索引值
        if  keys_pressed[pygame.K_RIGHT]:  # 理解？
            # print("向右")
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0



    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        enemies=pygame.sprite.spritecollide(self.hero,self.enemy_group,True)

        # if enemies:
        #     print("撞到了")  或者判断长度
        if  len(enemies) > 0:
            # 让英雄牺牲, 销毁对象
            self.hero.kill()
            #结束游戏
            PlanGame.__game_quit()
    def __update_sprites(self):
        self.background_group.update()
        self.background_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        # self.bullet_group.update()
        # self.bullet_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
    @staticmethod
    def  __game_quit():
        print("退出游戏")

        pygame.quit()
        exit()

if __name__ == '__main__':
    game=PlanGame()
    game.Gamestart()