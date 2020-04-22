import cv2, pafy

video=pafy.new('https://www.youtube.com/watch?v=zoP2vdNrOcE')
play=video.getbest(preftype='mp4') # webm any
capture=cv2.VideoCapture(play.url)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    success, frame = capture.read()
    if not success:
        break
    gray_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray_frame)
    for face in faces:
        x, y, w, h =face
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0), 3)
    cv2.imshow("fames : ",frame)
    cv2.waitKey(10)

    # cv2.imshow('Video',gray_frame)
    if cv2.waitKey(10)>0:
        break

cv2.destroyAllWindows()