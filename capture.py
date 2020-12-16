import cv2 , time , pandas
from datetime import datetime

first_frame  = None
status_list = [None,None]   #none and none added because during first iteration python is looking for 2 values and getting only 1
times = []
df = pandas.DataFrame(columns=["Start","End"])

video = cv2.VideoCapture(0,cv2.CAP_DSHOW) 
#zero for webcam:can add source of a video file as well
#second argument added after error on windows



while True:
    check , frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)           #refer opencv documentation
    
    #time.sleep(3) 
    #camera waits for 3s
    
    if first_frame is None:
        first_frame = gray
        continue
    
    #model takes first frame as reference and then whatever comes/moves after it is treated as an object
    delta_frame = cv2.absdiff(first_frame,gray)
    thresh_frame = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1] #opencv docs for different parameters to play with
    thresh_frame = cv2.dilate(thresh_frame,None,iterations = 2)
   
    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1

        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    status_list.append(status)
    
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())                  #checks when the object went in and out of frame and stores that time
    if status_list[-1]==0 and status_list[-2]==1:     #last and second last value of list is checked: 0 to 1 --> object came in frame and vice versa
        times.append(datetime.now())
    
    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Frame",frame)


    key = cv2.waitKey(1)
    #frame each 1ms
    
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows
