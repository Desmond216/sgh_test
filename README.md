# sgh_test

## 1. setting up python environment 
we would need anaconda prompt to run the jupyter notebook
use this command to 
 ```
 conda create -n sgh_env python=3.8 -y
 conda activate sgh_env
 pip install -r requirements.txt
 ```
 
 ## 2. run all cells in the jupyter notebook ```sgh_test``` 
 The jupyter notebook would train and save all the models, and also initialize the sqlite3 databases before using the app to make new prediction
 
 ## 3. Run the ```app.py```
 use this command to run the app
 ```
 streamlit run app.py
 ```
