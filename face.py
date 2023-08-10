import cv2
from deepface import DeepFace

camera = cv2.VideoCapture(0)

while True:
    _, img = camera.read()
        
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    cv2.imwrite("img.png", img)
    results = DeepFace.verify(img1_path='Zero.jpg', img2_path='img.jpg', enforce_detection=False)

    print(':)')


    cv2.imshow("image", img)


        
    if cv2.waitKey(1) == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
