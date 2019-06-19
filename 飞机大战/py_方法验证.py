import  pygame
pygame.init()
#print('游戏代码')
hero_rect=pygame.Rect(100,200,100,125)
print('英雄的原点:%d %d'%(hero_rect.x,hero_rect.y))
print("hero's  size is %d  %d"%(hero_rect.width,hero_rect.height))
print(hero_rect.center)
print(hero_rect.size)
pygame.quit()


