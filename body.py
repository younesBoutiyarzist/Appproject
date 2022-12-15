import pygame

class Body(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./assets/body.png')
        self.image = pygame.transform.scale(self.image, (171, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 230
        self.rect.y = 365
        self.x_origine = self.rect.x 
        self.y_origine = self.rect.y
        self.velocity = 5

    def move_right(self, pos, speed=0):
        if self.rect.x < self.x_origine + pos :
            self.rect.x += self.velocity
            self.rect.x += speed

    def move_left(self, pos, speed=0):
        if self.rect.x > self.x_origine + pos :
            self.rect.x -= self.velocity
            self.rect.x -= speed

    def move_up(self,pos, speed=0):
        if self.rect.y > self.y_origine + pos :
            self.rect.y -= self.velocity
            self.rect.y -= speed

    def move_down(self,pos, speed=0):
        if self.rect.y <self.y_origine + pos :
            self.rect.y += self.velocity
            self.rect.y += speed


        

