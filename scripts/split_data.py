import os 
import shutil 
import random 
import numpy as np

split_size = .15 
number_of_images = len(os.listdir(os.path.join(os.getcwd() , 'captured_data' , 'images')))
print(number_of_images)
val_images_num = int(np.floor(split_size * number_of_images) )
random_index = [random.randrange(1, number_of_images, 1) for i in range(val_images_num)] 

# move the val data 
for index in random_index : 
    images_list = os.listdir(os.path.join(os.getcwd() , 'captured_data' , 'images')) 
    image_path = os.path.join(os.getcwd() , 'captured_data' , 'images' , images_list[index] ) 
    label_file_name = os.path.join(os.getcwd() , 'captured_data' ,'labels' , images_list[index].split('.')[0]+'.json')
    shutil.move(image_path , os.path.join(os.getcwd(), 'labeled_data' , 'val' , 'images'))
    if os.path.exists(label_file_name) : 
        shutil.move(label_file_name , os.path.join(os.getcwd() , 'labeled_data' , 'val' ,'labels'))


print('this was the val data ') 

# move the rest of data 
for file in os.listdir(os.path.join(os.getcwd() , 'captured_data' , 'images')) : 
    image_path = os.path.join(os.getcwd() , 'captured_data' , 'images' , file) 
    label_file_name =  os.path.join(os.getcwd() , 'captured_data' , 'labels' , file.split('.')[0]+'.json' )
    shutil.move(image_path , os.path.join(os.getcwd(), 'labeled_data' , 'train' , 'images'))
    if os.path.exists(label_file_name) : 
        shutil.move(label_file_name , os.path.join(os.getcwd() , 'labeled_data' , 'train' ,'labels'))
