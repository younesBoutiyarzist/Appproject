# importing required library
import pygame

#import the avatar
from avatar import Avatar

import cv2
import mediapipe as mp
from datetime import datetime
import numpy as np
import time
import math 



# activate the pygame library .
i = 0
pygame.init()
X = 700
Y = 700
range_y_avatar = 65
range_y_face = 20
open_eyeL = True
open_eyeR = True
close_mouth = False

# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Avatar animation')

# create a surface object, image is drawn on it.
imp = pygame.image.load("./assets/all_body_parts.png").convert()

# Initialing RGB Color 
color = (255,255, 255)

# contain head
container = pygame.image.load("./assets/empty.png")
head_ctr = (container.get_width() / 2, container.get_height() / 2)
container_rect = container.get_rect(center=head_ctr)


# charge an avatar
avatar = Avatar()

while True:
    # Changing surface color
    scrn.fill(color)
    container = pygame.image.load("./assets/empty.png")

    # draw body
    scrn.blit(avatar.body.image, avatar.body.rect)

    # draw earR
    container.blit(avatar.earR.image, avatar.earR.rect)

    # draw earL
    container.blit(avatar.earL.image, avatar.earL.rect)

    # draw head
    container.blit(avatar.head.image, avatar.head.rect)

    # draw crow
    container.blit(avatar.crown.image, avatar.crown.rect)

    # draw eyeL
    container.blit(avatar.eyeL.image, avatar.eyeL.rect)

    # draw eyeR
    container.blit(avatar.eyeR.image, avatar.eyeR.rect)

    # draw mouth
    container.blit(avatar.mouth.image, avatar.mouth.rect)

    # draw moustacheR
    container.blit(avatar.moustacheR.image, avatar.moustacheR.rect)

    # draw moustacheL
    container.blit(avatar.moustacheL.image, avatar.moustacheL.rect)

    # check mouvement
    """if  y > 8 :
        avatar.translation_y(1, y, 3)
    if y < -8 :
        avatar.translation_y(0, y, 3)
    if  x > 8 :
        avatar.translation_x(1, -x, 3)
    if x < -8 :
        avatar.translation_x(0, -x, 3)
    if  z > 20 :
        avatar.rotation(0, z/2.5, 3)
    if z < -20 :
        avatar.rotation(1, z/2.5, 3)
    if y > -8 and y < 8 :
        avatar.center_y(3)
    if x > -8 and x < 8 :
        avatar.center_x(3)
    if z < 20 and z > -20 :
        avatar.center_z(5) """

    #avatar.moustacheL.rect.x > 50 and
    container = pygame.transform.rotate(container, -avatar.angle)
    container_rect = container.get_rect(center=head_ctr)
    scrn.blit(container, container_rect)

    pygame.display.flip()
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # Closing the window and program if the
        # type of the event is QUIT
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
            break

        # Checking event key if the type
        # of the event is KEYDOWN i.e.
        # keyboard button is pressed
        y = 0
        x = 0
        z = 0
        if event.type == pygame.KEYDOWN:
            y = y  + 4
            avatar.translation_y(1, y, 3)
        elif event.type == pygame.KEYUP:
            y = y  - 4
            avatar.translation_y(1, y, 3)
        

