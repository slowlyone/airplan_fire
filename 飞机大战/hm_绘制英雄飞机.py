import pygame

pygame.init()

screen=pygame.display.set_mode((480,700))
bg=pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
pygame.display.update()

hero=pygame.image.load("./images/me1.png")
screen.blit(hero,(200,500))
pygame.display.update()
clock=pygame.time.Clock()

while  True:
    clock.tick(60)
    pass

pygame.quit()
