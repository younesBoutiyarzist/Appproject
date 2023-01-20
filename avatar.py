import pygame
from eye import Eye
from ear import Ear
from head import Head
from crown import Crown
from moustache import Moustache
from mouth import Mouth
from body import Body


class Avatar:

    def __init__(self):

        self.angle = 0

        # eye L
        self.eyeL = Eye()
        self.eyeL.image = pygame.image.load('./assets/eyeL.png')
        self.eyeL.image = pygame.transform.scale(self.eyeL.image, (20, 64))
        self.eyeL.origine = self.eyeL.image 
        self.eyeL.rect = self.eyeL.image.get_rect()
        self.eyeL.rect.x = 275
        self.eyeL.rect.y = 255
        self.eyeL.x_origine = self.eyeL.rect.x 
        self.eyeL.y_origine = self.eyeL.rect.y 

        # eye R
        self.eyeR = Eye()
        self.eyeR.image = pygame.image.load('./assets/eyeR.png')
        self.eyeR.image = pygame.transform.scale(self.eyeR.image, (20, 64))
        self.eyeR.origine = self.eyeR.image 
        self.eyeR.rect = self.eyeR.image.get_rect()
        self.eyeR.rect.x = 335
        self.eyeR.rect.y = 255
        self.eyeR.x_origine = self.eyeR.rect.x 
        self.eyeR.y_origine = self.eyeR.rect.y 

        # ear L
        self.earL = Ear()
        self.earL.image = pygame.image.load('./assets/earL.png')
        self.earL.image = pygame.transform.scale(self.earL.image, (128, 200))
        self.earL.origine = self.earL.image 
        self.earL.rect = self.earL.image.get_rect()
        self.earL.rect.x = 135
        self.earL.rect.y = 45
        self.earL.x_origine = self.earL.rect.x 
        self.earL.y_origine = self.earL.rect.y 

        # ear R
        self.earR = Ear()
        self.earR.image = pygame.image.load('./assets/earR.png')
        self.earR.image = pygame.transform.scale(self.earR.image, (128, 200))
        self.earR.origine = self.earR.image 
        self.earR.rect = self.earR.image.get_rect()
        self.earR.rect.x = 380
        self.earR.rect.y = 50
        self.earR.x_origine = self.earR.rect.x 
        self.earR.y_origine = self.earR.rect.y 

        # moustache L
        self.moustacheL = Moustache()
        self.moustacheL.image = pygame.image.load('./assets/moustacheL.png')
        self.moustacheL.image = pygame.transform.scale(self.moustacheL.image, (171, 160))
        self.moustacheL.origine = self.moustacheL.image 
        self.moustacheL.rect = self.moustacheL.image.get_rect()
        self.moustacheL.rect.x = 85
        self.moustacheL.rect.y = 295
        self.moustacheL.x_origine = self.moustacheL.rect.x 
        self.moustacheL.y_origine = self.moustacheL.rect.y 

        # moustache R
        self.moustacheR = Moustache()
        self.moustacheR.image = pygame.image.load('./assets/moustacheR.png')
        self.moustacheR.image = pygame.transform.scale(self.moustacheR.image, (171, 160))
        self.moustacheR.origine = self.moustacheR.image 
        self.moustacheR.rect = self.moustacheR.image.get_rect()
        self.moustacheR.rect.x = 385
        self.moustacheR.rect.y = 290
        self.moustacheR.x_origine = self.moustacheR.rect.x 
        self.moustacheR.y_origine = self.moustacheR.rect.y 

        # Head
        self.head = Head()

        # Crown
        self.crown = Crown()
        
        # Head
        self.mouth = Mouth()

        # Body
        self.body = Body()
   
        # Buffer of action
        self.pressed = {}

    def translation_y(self, sens, pos, speed=0):
        if sens == 1:
            self.eyeL.move_right(pos, speed)
            self.eyeR.move_right(pos, speed)
            self.mouth.move_right(pos, speed)
            self.crown.move_right(pos, speed)
            self.moustacheL.move_right(pos, speed)
            self.moustacheR.move_right(pos, speed)
        elif sens == 0:
            self.eyeL.move_left(pos, speed)
            self.eyeR.move_left(pos, speed)
            self.mouth.move_left(pos, speed)
            self.crown.move_left(pos, speed)
            self.moustacheL.move_left(pos, speed)
            self.moustacheR.move_left(pos, speed)

    def translation_x(self, sens, pos, speed=0):
        if sens == 1:
            self.eyeL.move_up(pos, speed)
            self.eyeR.move_up(pos, speed)
            self.mouth.move_up(pos, speed)
            self.moustacheL.move_up(pos, speed)
            self.moustacheR.move_up(pos, speed)
            self.crown.move_up(pos, speed)
        elif sens == 0:
            self.eyeL.move_down(pos, speed)
            self.eyeR.move_down(pos, speed)
            self.mouth.move_down(pos, speed)
            self.crown.move_down(pos, speed)
            self.moustacheL.move_down(pos, speed)
            self.moustacheR.move_down(pos, speed)


    def rotation(self, sens, angle,  speed=1):
        if sens == 1 and angle < self.angle :
            self.angle -= speed
        if sens == 0 and angle >self.angle :
            self.angle += speed
    
    def center_y(self, speed=0):
        if self.eyeR.rect.x - self.eyeR.x_origine > 0:
            self.translation_y(0, 0, speed)
        else :
            self.translation_y(1, 0, speed)

    def center_x(self, speed=0):
        if self.eyeR.rect.y - self.eyeR.y_origine < 0:
            self.translation_x(0, 0, speed)
        else :
            self.translation_x(1, 0, speed)

    def center_z(self, speed=0):
        if self.angle > speed + 1:
            self.angle -= speed
        elif self.angle < -speed - 1:
            self.angle += speed
        else :
            self.angle = 0
        


       
                




