import pygame

class Ear(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = None
        self.rect = None
        self.origine = None
        self.velocity = 1
        self.x_origine = None
        self.y_origine = None
        self.angle = 0
        self.scale_x = 1.0

    def move_right(self, pos, speed=0):
        self.rect.x += self.velocity
        self.rect.x += speed

    def move_left(self, pos, speed=0):
        self.rect.x -= self.velocity
        self.rect.x -= speed

    def move_up(self,pos, speed=0):
            self.rect.y -= self.velocity
            self.rect.y -= speed

    def move_down(self,pos, speed=0):
            self.rect.y += self.velocity
            self.rect.y += speed

    def move_rotation_p(self, speed=1,x=None, y=None):
        self.angle += speed
        if x == None:
            x = self.rect.x + (self.image.get_width()/2)
            y = self.rect.y + (self.image.get_height()/2)
        self.image = pygame.transform.rotate(self.origine, self.angle)
        self.rect = self.image.get_rect(center = self.image.get_rect(center = (x, y)).center)

    def move_rotation_m(self, speed=1, x=None, y=None):
        self.angle -= speed
        if x == None:
            x = self.rect.x + (self.image.get_width()/2)
            y = self.rect.y + (self.image.get_height()/2)
        self.image = pygame.transform.rotate(self.origine, self.angle)
        self.rect = self.image.get_rect(center = self.image.get_rect(center = (x, y)).center)

