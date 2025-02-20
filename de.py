import cv2

face_cascade = cv2.CascadeClassifier(r'C:\Users\sahit\Downloads\haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier(r'C:\Users\sahit\Downloads\haarcascade_eye.xml') 
smile_cascade = cv2.CascadeClassifier(r'C:\Users\sahit\Downloads\haarcascade_smile.xml')  


def detect(grayimage,colorimage):
    faces = face_cascade.detectMultiScale(grayimage, 1.3, 5) 
    for (x,y,w,h) in faces:
        cv2.rectangle(colorimage,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = grayimage[y:y+h, x:x+w]
        roi_color = colorimage[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray,1.1,22)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        smiles = smile_cascade.detectMultiScale(roi_gray,1.7,25)
        for (sx,sy,sw,sh) in smiles:
            cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)
    return colorimage

cap = cv2.VideoCapture(0)

while 1:
    _,c_img = cap.read()
    gray_image = cv2.cvtColor(c_img, cv2.COLOR_BGR2GRAY) 
    result = detect(gray_image,c_img)
    cv2.imshow('Video',result)

    if cv2.waitKey(1) & 0xFF==ord('x'):
        break

cap.release() 
            
cv2.destroyAllWindows() 
    
