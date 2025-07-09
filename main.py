import pygame

win = pygame.display.set_mode((700, 500))

clock = pygame.time.Clock()

win.fill((0, 220, 255))

is_game = True

class GameSprite(pygame.sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = pygame.transform.scale(pygame.image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       win.blit(self.image, (self.rect.x, self.rect.y))

class player(GameSprite):
    def update_r(Self)
        key = pygame.getpressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]and self.rect.y < 415:
            self.rect.y += self.speed
     def update_l(Self)
        key = pygame.getpressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s]and self.rect.y < 415:
            self.rect.y += self.speed


while is_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game = False

    pygame.display.update()
    clock.tick(40)