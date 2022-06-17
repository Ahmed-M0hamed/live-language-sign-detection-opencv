import tensorflow as tf 
import numpy as np 
import cv2 
import os 

model = tf.keras.models.load_model('F:/react-sign-detection/modeling/facetracker_1')

classes_dict = {
    0 :  'empty' ,   
    1 : 'high-five' , 
    2 : 'peace' , 
    3 : 'good-luck' ,   
    4 : 'f-you'  ,
    5 : 'whats-up'

}

cap = cv2.VideoCapture(0) 
while cap.isOpened() : 
    _ , frame = cap.read()
    frame = frame[50:500, 50:500,:]

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resized = tf.image.resize(rgb, (120,120))
    
    yhat = model.predict(np.expand_dims(resized/255,0))
#     print(yhat)
    sample_coords = yhat[1][0]
    
    sign_name = tf.math.argmax(yhat[0][0]).numpy()

    if sign_name != 0 : 
        # Controls the main rectangle
        cv2.rectangle(frame, 
                    tuple(np.multiply(sample_coords[:2], [450,450]).astype(int)),
                    tuple(np.multiply(sample_coords[2:], [450,450]).astype(int)), 
                            (255,0,0), 2)
        # Controls the label rectangle
        cv2.rectangle(frame, 
                    tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int), 
                                    [0,-30])),
                    tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int),
                                    [80,0])), 
                            (255,0,0), -1)
        
#         Controls the text rendered
        cv2.putText(frame,classes_dict[sign_name] , tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int),
                                            [0,-5])),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
    
    cv2.imshow('EyeTrack', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()