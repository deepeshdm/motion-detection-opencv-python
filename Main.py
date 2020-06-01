import cv2 as cv

#Enter the video file
cap = cv.VideoCapture('vtest.avi')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours :
        (x,y,w,h)=cv.boundingRect(contour)

         #Enter the minimum size of object to be tracked for motion
        if cv.contourArea(contour) < 900:
            continue

        cv.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv.putText(frame1,"status:".format('movement'),(10,20),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)


    cv.imshow('feed', frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    cv.waitKey(0)


cv.destroyAllWindows()
cv.release()
