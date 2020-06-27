#This program detects faces in real time and if a face is found changes the output color from gray to the actual color and makes a sound
#this is particularly helpful in scenarios where there is a continuous feed for hours without no person(night time) and displaying color takes more energy. 
#to color of the outputthough the training set is quite small*/

import cv2,time #OpenCV has been used
import winsound #For creating sound when face is detected.
face_cascade=cv2.CascadeClassifier("C:\\Users\\haarcascade_frontalface_default.xml") #Enter the path where you have saved the XML containing the training set
video=cv2.VideoCapture(0) #Switch on webcam
while True:
  check,frame=video.read() #Frame is the current frame, Check is a boolean which checks if video is still working
  print(check)  
  print(frame) #Printing these for reference
  
  gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Converting the frame to grayscale in case there is No face.
  faces=face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5) #run the gray image through the face_casecade to detect faces.
  
  for x,y,w,h in faces:
    gray=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,2,3)) #Setting up the green color rectangle ( width and height) and assigning the frame to gray variable
	duration = 50  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration) #make sound when face seen
  cv2.imshow("Capturing",gray) #The window where you see the output

  key=cv2.waitKey(1) #will display a frame for 1 ms, after which display will be automatically closed
  if key==ord('q'): #exit when q is pressed
    break
video.release() #Switch off webcam
cv2.destroyAllWindows