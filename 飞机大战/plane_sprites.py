import random
import pygame

#屏幕大小
GAME_RECT=pygame.Rect(0,0,400,500)
#时钟频率
TIME_BIT=60
GREATE_EVEM_EVENT=pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT +1
class GameSprite(pygame.sprite.Sprite):
    ''' 飞机大战游戏精灵'''
    def __init__(self,image_name,speed=1):
        super().__init__()
        self.image=pygame.image.load(image_name)
        self.rect=self.image.get_rect()
        self.speed=speed
        # self.speed=random.randint(1,4)
        # self.sitebit=random.randint(0, GAME_RECT.width)
    def update(self):

        # self.rect.x = self.sitebit
        self.rect.y += self.speed
        # if self.rect.y == GAME_RECT.height:
        #     #删除
        #     pass

class Background(GameSprite):
    def __init__(self,speed=1,is_alt=0):
        super().__init__("./images/background.png")
        # self.image=pygame.image.load("./images/background.png")
        # self.rect=self.image.get_rect()
        self.speed=speed

        if is_alt==1:
            self.rect.y=-self.rect.height

    def update(self):
        self.rect.y +=self.speed
        #判断是否移出屏幕
        if self.rect.y >= GAME_RECT.height:
            self.rect.y = -GAME_RECT.height

class Enemy(GameSprite):
    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed=random.randint(1,4)
        self.position_x=random.randint(0,GAME_RECT.width-self.rect.width)
        # self.rect.y = - self.rect.height     #美化效果
        self.rect.bottom =0
    def update(self):
        self.rect.y += self.speed
        self.rect.x = self.position_x

        if self.rect.y >= GAME_RECT.height:   #>=比==好，因为有些销毁时y坐标还是500+1
            # print("到低了")
            self.kill() #kill将精灵从所有组中移出，精灵会自动销毁
            # pygame.sprite.Group(delattr(self))
            # self.__del__()
class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/me1.png",0)

        self.rect.centerx=GAME_RECT .centerx
        self.rect.y=GAME_RECT.bottom - 120
        #3 创建子弹对精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x <=0:
            self.rect.x =0
        # elif self.rect.x >=GAME_RECT.width - self.rect.width
        elif self.rect.right > GAME_RECT.right:
            self.rect.right = GAME_RECT.right

    def  fire(self):
        # print("发射子弹")
        for i in (0,1,2):
            # 1.创建子弹精灵
            bullet = Bullet()
            #2.设置精灵位置
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx= self.rect.centerx
            #3 将精灵添加到精灵组
            self.bullets.add(bullet)

    def __del__(self): # 一旦销毁 就会被调用
        #print("敌机挂了 %s"%self.rect)
        pass

# personal code

class  Bullet(GameSprite):
    #子弹精灵类
    def __init__(self):
        #调用父类初始化方法，设置子弹图片和初始速度
        super().__init__("./images/bullet1.png",-2)
        # self.rect.centerx=

    def update(self):
        # 调用父类方法，设置子弹向上飞行
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.y <= 0:
            self.kill()

    def __del__(self):
        print("子弹已经销毁 %s" %self.rect)
