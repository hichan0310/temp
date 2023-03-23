import pygame
import sys
import random
from src.player import Player
from src.bullet import Bullet

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
player_group= pygame.sprite.Group()
player = Player(player_group, (400, 500))

bullet_group = pygame.sprite.Group()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('gray')



    Bullet(bullet_group, (random.randint(0, 800), 0))
    bullet_group.update()
    bullet_group.draw(screen)


    player_group.update()
    player.check_collide(bullet_group)
    player_group.draw(screen)

    pygame.display.update()
    clock.tick(60)