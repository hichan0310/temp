import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, group, center):
        super().__init__(group)
        self.image=pygame.image.load("./img/bullet.png").convert_alpha()
        self.rect=self.image.get_rect(center=center)
        self.hitbox=pygame.rect.Rect(0, 0, 10, 10)
        self.position=pygame.math.Vector2(center)
        self.direction=pygame.math.Vector2((0, 5))

    def update(self):
        self.position += self.direction
        self.rect.center = self.position
        if self.rect.right<0 or \
            self.rect.left>800 or \
            self.rect.top<0 or \
            self.rect.bottom>600:
            self.kill()
        self.hitbox.center=self.position