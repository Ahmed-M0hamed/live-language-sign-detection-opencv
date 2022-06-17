import cv2 
import uuid 
import os 
import time 
path = os.path.join(os.getcwd() , 'captured_data' , 'images')
cap = cv2.VideoCapture(0)
for i in range(20) : 
    _ , frame = cap.read() 
    cv2.imwrite(os.path.join(path , f'{str(uuid.uuid1())}.jpg') , frame)
    cv2.imshow('frame', frame)
    time.sleep(0.5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()