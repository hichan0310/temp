import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, group, center):
        super().__init__(group)
        self.image=pygame.image.load("./img/player.png").convert_alpha()
        self.rect=self.image.get_rect(center=center)
        self.hitbox=pygame.rect.Rect(0, 0, 10, 10)
        self.position=pygame.math.Vector2(center)
        self.hitbox.center=self.position
        self.speed=8

    def check_bounds(self):
        self.position.x=max(self.position.x, 20)
        self.position.x=min(self.position.x, 780)
        self.position.y=max(self.position.y, 30)
        self.position.y=min(self.position.y, 570)

    def check_collide(self, bullet_group):
        for sprite in bullet_group.sprites():
            if self.hitbox.colliderect(sprite.hitbox):
                self.kill()

    def update(self):
        keys = pygame.key.get_pressed()

        direction = pygame.math.Vector2((0, 0))
        direction.x = keys[pygame.K_RIGHT]-keys[pygame.K_LEFT]
        direction.y = keys[pygame.K_DOWN]-keys[pygame.K_UP]
        if not direction:   #0벡터 검사
            return
        direction=direction.normalize()     # 대각선 때문에 사용됨, 방향을 동일하게 한 상태에서 크기를 1로
        self.position += direction*self.speed
        self.check_bounds()
        self.rect.center = self.position
        self.hitbox.center=self.position