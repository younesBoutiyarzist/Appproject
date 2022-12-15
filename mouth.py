import pygame

class Mouth(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./assets/mouth.png')
        self.image = pygame.transform.scale(self.image, (40, 23))
        self.origine = self.image
        self.angle = 0
        self.rect = self.image.get_rect()
        self.rect.x = 292
        self.rect.y = 335
        self.x_origine = self.rect.x 
        self.y_origine = self.rect.y
        self.velocity = 1

    def move_right(self, pos, speed=0):
        if self.rect.x < self.rect.x + pos :
            self.rect.x += self.velocity
            self.rect.x += speed

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

    def move_rotation_p(self, speed=1,x=None,y=None):
        self.angle += speed
        if x == None:
            x = self.rect.x + (self.image.get_width()/2)
            y = self.rect.y + (self.image.get_height()/2)
        self.image = pygame.transform.rotate(self.origine, self.angle)
        self.rect = self.image.get_rect(center = self.image.get_rect(center = (x, y)).center)

    def move_rotation_m(self, speed=1,x=None,y=None):
        self.angle -= speed
        if x == None:
            x = self.rect.x + (self.image.get_width()/2)
            y = self.rect.y + (self.image.get_height()/2)
        self.image = pygame.transform.rotate(self.origine, self.angle)
        self.rect = self.image.get_rect(center = self.image.get_rect(center = (x, y)).center)

 

