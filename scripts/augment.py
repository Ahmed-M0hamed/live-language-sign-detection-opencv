import albumentations as alb 
import os 
import uuid
import cv2 
import json 
import numpy as np 

# define the generator 
augmentor = alb.Compose([alb.HorizontalFlip(p=0.5), 
                         alb.RandomBrightnessContrast(p=0.2),
                         alb.RandomGamma(p=0.2), 
                         alb.RGBShift(p=0.2), 
                         alb.VerticalFlip(p=0.5)], 
                       bbox_params=alb.BboxParams(format='albumentations', 
                                                label_fields=['class_labels']))

classes_dict = {
    'empty' : 0 , 
    'high-five' : 1 ,
    'peace' : 2 , 
    'good-luck' : 3 , 
    'f-you' : 4 , 
    'whats-up' : 5

}

for partition in ['train','val']: 
    for image in os.listdir(os.path.join( os.getcwd(),'labeled_data', partition, 'images')):
        img = cv2.imread(os.path.join(os.getcwd(), 'labeled_data', partition, 'images', image))

        coords = [0,0,0.00001,0.00001]
        label_name = ''
        label_path = os.path.join( os.getcwd(),'labeled_data', partition, 'labels', f'{image.split(".")[0]}.json')
        if os.path.exists(label_path):
            with open(label_path, 'r') as f:
                label = json.load(f)

            coords[0] = label['shapes'][0]['points'][0][0]
            coords[1] = label['shapes'][0]['points'][0][1]
            coords[2] = label['shapes'][0]['points'][1][0]
            coords[3] = label['shapes'][0]['points'][1][1]
            coords = list(np.divide(coords, [640,480,640,480]))
            # (width , height ) this the width and height of your images 
            # so if you changed it in the script update it 

            label_name = label['shapes'][0]['label']


        try: 
            for x in range(60):

                augmented = augmentor(image=img, bboxes=[coords], class_labels=[label_name])
                cv2.imwrite(os.path.join( os.getcwd(),'aug_data', partition, 'images', f'{image.split(".")[0]}.{x}.jpg'), augmented['image'])

                annotation = {}
                annotation['image'] = image

                if os.path.exists(label_path):
                    if len(augmented['bboxes']) == 0: 
                        annotation['bbox'] = [0,0,0,0]
                        annotation['class'] = classes_dict['empty']
                    else: 
                        annotation['bbox'] = augmented['bboxes'][0]
                        annotation['class'] = classes_dict[label_name]
                else: 
                    annotation['bbox'] = [0,0,0,0]
                    annotation['class'] = classes_dict['empty'] 


                with open(os.path.join(os.getcwd(), 'aug_data', partition, 'labels', f'{image.split(".")[0]}.{x}.json'), 'w') as f:
                    json.dump(annotation, f)

        except Exception as e:
            print(e)