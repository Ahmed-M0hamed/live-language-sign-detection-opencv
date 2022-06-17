import os 

# resized_data dir 
os.makedirs(os.path.join(os.getcwd() , 'captured_data')) 
os.makedirs(os.path.join(os.getcwd() , 'captured_data' , 'images')) 
os.makedirs(os.path.join(os.getcwd() , 'captured_data' , 'labels')) 

# data 
splits = ['train' , 'val']
os.makedirs(os.path.join(os.getcwd() , 'labeled_data'))  
for split in splits : 
    os.makedirs(os.path.join(os.getcwd() , 'labeled_data', split)) 
    os.makedirs(os.path.join(os.getcwd() ,'labeled_data',  split , 'images')) 
    os.makedirs(os.path.join(os.getcwd() ,'labeled_data',split , 'labels')) 

# aug_data 

os.makedirs(os.path.join(os.getcwd() , 'aug_data'))  
for split in splits : 
    os.makedirs(os.path.join(os.getcwd() , 'aug_data', split)) 
    os.makedirs(os.path.join(os.getcwd() ,'aug_data',  split , 'images')) 
    os.makedirs(os.path.join(os.getcwd() ,'aug_data',split , 'labels')) 

