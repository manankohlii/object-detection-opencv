import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#this xml file is for faces, for others checkout opencv ki git repo

img = cv2.imread("photo.jpg")

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,
scaleFactor=1.05,
minNeighbors=5)
#play with diff values of sf and mn : for news.jpg 
#it detects the hand as a face for sf=1.05 but not for sf = 1.1

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
#x y w h are the 4 values in the numpy array 'faces' for an individual face
print(faces)

resized = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow("gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
