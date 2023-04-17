#%%
import cv2 as cv 

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("haarcascade_eye.xml")
# %%
img = cv.imread('image.jpg')
#%%
# convert to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect faces of the grey image
# the 5 is the 'n' neighbors used to detecting multiple faces
faces = face_cascade.detectMultiScale(gray,1.3,5)

# print number of faces
print(len(faces))

#%%
# get x,y coordinate and the width/height of the faces
# this the x,y values are the left corner of the blue rectangles, 
# from there we add the width and height where the face is found to draw the square

for (x,y,w,h) in faces:
    # (x,y)/(x+w,y+h) : all the points of the face , color of rectangle: (255,0,0), and 2 is the thickness of the lines
    cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)
    eye_gray = gray[y:y+h, x:x+w]
    #
    eye_color = img[y:y+h, x:x+w]
    # detect where the eyes are
    eyes = eye_cascade.detectMultiScale(eye_gray)
    # using a for loop to get the 4 points
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(eye_color, (ex,ey), (ex+ew, ey+eh), (0,255,0),2)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()

# %%
