# sgh_test

## System Design 

This is the diagram for the system design of this project under few assumptions:

 1) The data source is a one time csv indicating that there's no continuous flow of raw data either in batches or real-time streaming, 
    hence, there's no need to include scheduler such as Airflow to schedule data pipeline for batch processing
 
 2) There's no requirement to deploy the data pipeline and application on cloud platform such as Azure, AWS or GCP. We would deploy everything in local environment under Windows OS
 
 

![image](https://user-images.githubusercontent.com/27355460/218440833-dc6846e7-8c26-4a87-b22b-f02b58870016.png)

### Workflow
 1) Data from csv is analysed and processed in jupyter notebook
 2) Processed data is used to train machine learning models and the models are saved
 3) Jupyter notebook initialises database to store processed data in normalised tables and set up logging table
 4) The hosted app is able to receive user input and call model api to make prediction with the given input and show prediction result
 5) User input data is saved in logging table and the data is available on the app





## 1. Setting up python environment 
we would need anaconda prompt to run the jupyter notebook

after cloning the project, go to the directory and use this command or other equivalent command to set up the python environment and install dependencies for the project
 ```
 conda create -n sgh_env python=3.8 -y
 conda activate sgh_env
 pip install -r requirements.txt
 ```
 
 ## 2. Run all cells in the jupyter notebook ```sgh_test``` 
 The jupyter notebook would train and save all the models, and also initialize the sqlite3 databases before using the app to make new prediction
 
 ## 3. Run the ```app.py```
 use this command to run the app in the anaconda prompt
 ```
 streamlit run app.py
 ```
 
 Input new patient data to make prediction
 
 ![image](https://user-images.githubusercontent.com/27355460/218432438-2c7c3771-85c2-40f4-8714-ba5842719c44.png)
 
 Check input logs in another tab
 
 ![image](https://user-images.githubusercontent.com/27355460/218432925-9fb7bec1-151c-483e-b024-d0ab2cbd7fbd.png)


