# sign detection 
this opencv app for live language sign detection 

# how the app work 
- we gathered images with opencv through the webcam 
- we labeled the data and augmented it with python modules 
- we trained model for the job  

# how to run the app 
- clone the repo 
```bash 
git clone repo 
cd repo 
pip install -r requirements.txt
``` 

- structure the project 
```bash 
python scripts/create_dirs.py
```

- capture the data 

```bash 
python scripts/capture.py
```
- label the data
open the notebook and run the labelme cell to triger the api 
and you have to labels the images you select the resized_data/images dir 
and at the top left corner from the drop list select change output dir 
and select resized_data/labels and from the drop list click save automaticly 
after that from the next drop list select draw rectangle and start label your images 

- split the data 
```bash 
python scripts/split.py 
```

- augment the data 
```bash 
python scripts/augment.py 
``` 

- train the model 
open the note book and run the cells to train the model 

- detect through the webcam 
```bash 
python scripts/live-detection.py 
``` 

you will be able to detect some thing like that 


