import cv2
import numpy as np

 # font
font = cv2.FONT_HERSHEY_SIMPLEX
  
# org
org = (50, 50)
  
# fontScale
fontScale = 1
   
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2

# Create point matrix get coordinates of mouse click on image
point_matrix = np.zeros((2,2),np.int)
part = ['head','eye_R','eye_L','ear_R','ear_L','hat','mouth','moustache_R','moustache_L']
part_data = np.zeros((2,2, len(part)),np.int)
part_counter = 0
counter = 0
def mousePoints(event,x,y,flags,params):
    global counter
    # Left button mouse click event opencv
    if event == cv2.EVENT_LBUTTONDOWN:
        point_matrix[counter] = x,y
        counter = counter + 1
 
# Read image
img = cv2.imread('./assets/fuwa_glace.png')
dimensions = img.shape
img = cv2.resize(img, (round(dimensions[0]/3), round(dimensions[1]/3))) 
while True:
    for x in range (0,2):
        cv2.circle(img,(point_matrix[x][0],point_matrix[x][1]),3,(0,255,0),cv2.FILLED)
 
    if counter == 2:
        starting_x = point_matrix[0][0]
        starting_y = point_matrix[0][1]
 
        ending_x = point_matrix[1][0]
        ending_y = point_matrix[1][1]
        # Draw rectangle for area of interest
        cv2.rectangle(img, (starting_x, starting_y), (ending_x, ending_y), (0, 255, 0), 3)
 
        # Cropping image
        img_cropped = img[starting_y:ending_y, starting_x:ending_x]
        part_data[:,:,part_counter] = point_matrix
        cv2.imshow(part[part_counter], img_cropped)
        if part[part_counter] == 'head':
            blank_image1 = np.zeros((round(dimensions[0]/3), round(dimensions[1]/3),3), np.uint8)
            blank_image2 = np.zeros((round(dimensions[0]/3), round(dimensions[1]/3),3), np.uint8)
            blank_image1[point_matrix[0][1]:point_matrix[1][1], point_matrix[0][0]:point_matrix[1][0]] = img_cropped
        else:
            blank_image1[max(point_matrix[0][1],part_data[0,1,0]) :min(point_matrix[1][1],part_data[1,1,0]) , max(point_matrix[0][0],part_data[0,0,0]) :min(point_matrix[1][0],part_data[1,0,0]) ] = (255,255,255)
            blank_image2[max(point_matrix[0][1],part_data[0,1,0]) :min(point_matrix[1][1],part_data[1,1,0]) , max(point_matrix[0][0],part_data[0,0,0]) :min(point_matrix[1][0],part_data[1,0,0]) ] = (255,255,255)
        if part_counter == len(part) -1:
            cv2.imwrite('./test/imageToImpaint.png', blank_image1)
            cv2.imwrite('./test/mask.png', blank_image2)




    
    img_n = cv2.putText(img, 'select ' + part[part_counter], org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
    
    # Showing original image
    cv2.imshow("Original Image ", img_n)
    
    # Mouse click event on original image
    cv2.setMouseCallback("Original Image ", mousePoints)
    # Printing updated point matrix
    print(point_matrix)
    # Refreshing window all time
    if counter == 2:
        counter = 0
        part_counter = part_counter + 1
        if part_counter == len(part):
            break
    cv2.waitKey(1)
cv2.destroyAllWindows()

