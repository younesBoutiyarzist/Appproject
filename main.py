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

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
init_horizon = 0

cap = cv2.VideoCapture(0)

# activate the pygame library .
pygame.init()
X = 700
Y = 700
range_y_avatar = 65
range_y_face = 20
open_eyeL = True
open_eyeR = True

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

status = True
while cap.isOpened():

    success, image = cap.read()

    start = time.time()

    # Flip the image horizontally for a later selfie-view display
    # Also convert the color space from BGR to RGB
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

    # To improve performance
    image.flags.writeable = False
    
    # Get the result
    results = face_mesh.process(image)
    
    # To improve performance
    image.flags.writeable = True
    
    # Convert the color space from RGB to BGR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    img_h, img_w, img_c = image.shape
    face_3d = []
    face_2d = []

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            for idx, lm in enumerate(face_landmarks.landmark):
                if idx == 33 or idx == 263 or idx == 1 or idx == 61 or idx == 291 or idx == 199:
                    if idx == 1:
                        nose_2d = (lm.x * img_w, lm.y * img_h)
                        nose_3d = (lm.x * img_w, lm.y * img_h, lm.z * 3000)

                    x, y = int(lm.x * img_w), int(lm.y * img_h)

                    # Get the 2D Coordinates
                    face_2d.append([x, y])

                    # Get the 3D Coordinates
                    face_3d.append([x, y, lm.z])       
            
            # Convert it to the NumPy array
            face_2d = np.array(face_2d, dtype=np.float64)

            # Convert it to the NumPy array
            face_3d = np.array(face_3d, dtype=np.float64)

            # The camera matrix
            focal_length = 1 * img_w

            cam_matrix = np.array([ [focal_length, 0, img_h / 2],
                                    [0, focal_length, img_w / 2],
                                    [0, 0, 1]])

            # The distortion parameters
            dist_matrix = np.zeros((4, 1), dtype=np.float64)

            # Solve PnP
            success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)

            # Get rotational matrix
            rmat, jac = cv2.Rodrigues(rot_vec)

            # Get angles
            angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)

            # Get the y rotation degree
            x = angles[0] * 360
            y = angles[1] * 360
            z = angles[2] * 360

            range_eyeL = math.sqrt(math.pow(face_landmarks.landmark[159].x - face_landmarks.landmark[145].x, 2) + math.pow(face_landmarks.landmark[159].y - face_landmarks.landmark[145].y, 2))
            range_eyeR = math.sqrt(math.pow(face_landmarks.landmark[386].x - face_landmarks.landmark[374].x, 2) + math.pow(face_landmarks.landmark[386].y - face_landmarks.landmark[374].y, 2))

            # See where the user's head tilting
            if y < -10:
                text = "Looking Left"
            elif y > 10:
                text = "Looking Right"
            elif x < -10:
                text = "Looking Down"
            elif x > 10:
                text = "Looking Up"
            else:
                text = "Forward"

            # Display the nose direction
            nose_3d_projection, jacobian = cv2.projectPoints(nose_3d, rot_vec, trans_vec, cam_matrix, dist_matrix)

            p1 = (int(nose_2d[0]), int(nose_2d[1]))
            p2 = (int(nose_2d[0] + y * 10) , int(nose_2d[1] - x * 10))
            
            cv2.line(image, p1, p2, (255, 0, 0), 3)

            # Add the text on the image
            cv2.putText(image, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
            cv2.putText(image, "x: " + str(np.round(x,2)), (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(image, "y: " + str(np.round(y,2)), (500, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(image, "z: " + str(np.round(z,2)), (500, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


        end = time.time()
        totalTime = end - start

        fps = 1 / totalTime
        #print("FPS: ", fps)

        cv2.putText(image, f'FPS: {int(fps)}', (20,450), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)

        mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=drawing_spec,
                    connection_drawing_spec=drawing_spec)


    cv2.imshow('Head Pose Estimation', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

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
    if  y > 8 :
        avatar.translation_y(1, y, 10)
    if y < -8 :
        avatar.translation_y(0, y, 10)
    if  x > 8 :
        avatar.translation_x(1, -x,10)
    if x < -8 :
        avatar.translation_x(0, -x, 10)
    if y > -8 and y < 8 :
        avatar.center_y(10)
    if x > -8 and x < 8 :
        avatar.center_x(10)
    if range_eyeL < 0.01 and open_eyeL :
        old_size = avatar.eyeL.image.get_width()
        avatar.eyeL.image = pygame.transform.scale(avatar.eyeL.image, (avatar.eyeL.origine.get_width(), round(avatar.eyeL.origine.get_height()/2)))
        avatar.eyeL.rect.y += old_size/ 2
        open_eyeL = False
    if range_eyeL > 0.01 and not open_eyeL :
        old_size = avatar.eyeL.image.get_width()
        avatar.eyeL.image = pygame.transform.scale(avatar.eyeL.image, (avatar.eyeL.origine.get_width(), round(avatar.eyeL.origine.get_height())))
        avatar.eyeL.rect.y -= old_size/ 2
        open_eyeL = True
    if range_eyeR < 0.01 and open_eyeR :
        old_size = avatar.eyeL.image.get_width()
        avatar.eyeR.image = pygame.transform.scale(avatar.eyeR.image, (avatar.eyeR.origine.get_width(), round(avatar.eyeR.origine.get_height()/2)))
        avatar.eyeR.rect.y += old_size/ 2
        open_eyeR = False
    if range_eyeR > 0.01 and not open_eyeR :
        old_size = avatar.eyeR.image.get_width()
        avatar.eyeR.image = pygame.transform.scale(avatar.eyeR.image, (avatar.eyeR.origine.get_width(), round(avatar.eyeR.origine.get_height())))
        avatar.eyeR.rect.y -= old_size/ 2
        open_eyeR = True
    
    

#avatar.moustacheL.rect.x > 50 and
    container = pygame.transform.rotate(container, avatar.angle)
    container_rect = container.get_rect(center=head_ctr)
    if avatar.pressed.get(pygame.K_RIGHT):
        print(open_eyeL)
        if open_eyeL:
            old_size = avatar.eyeL.image.get_width()
            avatar.eyeL.image = pygame.transform.scale(avatar.eyeL.image, (avatar.eyeL.origine.get_width(), round(avatar.eyeL.origine.get_height())))
            avatar.eyeL.rect.y -= old_size/ 2
            open_eyeL = True
            print(open_eyeL)
            
        #if avatar.moustacheR.rect.x < 425:
        #avatar.translation_x(1, -20)
        #container = pygame.transform.rotate(container, avatar.angle)
        #container_rect = container.get_rect(center=head_ctr)
    elif avatar.pressed.get(pygame.K_LEFT):
        print(open_eyeL)
        if not open_eyeL:
            old_size = avatar.eyeL.image.get_width()
            avatar.eyeL.image = pygame.transform.scale(avatar.eyeL.image, (avatar.eyeL.origine.get_width(), round(avatar.eyeL.origine.get_height())))
            avatar.eyeL.rect.y -= old_size/ 2
            open_eyeL = True
            print(open_eyeL)

            

    elif avatar.pressed.get(pygame.K_UP):
        avatar.rotation(1)
        container = pygame.transform.rotate(container, avatar.angle)
        container_rect = container.get_rect(center=head_ctr)
    elif avatar.pressed.get(pygame.K_DOWN):
        avatar.rotation(0)

        container = pygame.transform.rotate(container, avatar.angle)
        container_rect = container.get_rect(center=head_ctr)
    else:
        container = pygame.transform.rotate(container, avatar.angle)
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
        if event.type == pygame.KEYDOWN:
            avatar.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            avatar.pressed[event.key] = False

cap.release()
       


# deactivates the pygame library
pygame.quit()
