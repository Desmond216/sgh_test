
import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import joblib

def model_api(model_name, *args):
    model = joblib.load(f'models/{model_name}.joblib')
    parameters = pd.DataFrame({'Age':[args[0]], 'AgeGroup':[args[1]], 'Sex':[args[2]], 'Infection':[args[3]], 'SysBP':[args[4]], 'Pulse':[args[5]], 'Emergency':[args[6]]})
    survive = model.predict(parameters)[0]
    prob = int(np.max(model.predict_proba(parameters))*100)
    if survive:
        return f'predicted survive with probability: {prob}%'
    else:
        return f'predicted not survive with probability: {prob}%'

def logging(*args):
    conn = sqlite3.connect('sgh.db')
    parameters = pd.DataFrame({'ID':[args[7]], 'Age':[args[0]], 'AgeGroup':[args[1]], 'Sex':[args[2]], 'Infection':[args[3]], 'SysBP':[args[4]], 'Pulse':[args[5]], 'Emergency':[args[6]]})
    parameters.to_sql('logging', con=conn, if_exists='append', index=False)
    conn.close()
    return

def show_logs():
    conn = sqlite3.connect('sgh.db')
    logs = pd.read_sql('SELECT * FROM logging', con=conn)
    conn.close()
    return logs


def main():

    #app layout
    tab_selected = st.sidebar.selectbox("Select a tab", ["Predict new patient survival probability", "View logs"])

    if tab_selected == "Predict new patient survival probability":

        st.title("Enter data to predict new patient survival probability")
        Id = st.text_input("ID", "")
        age = st.number_input("Age", value=18, min_value=0, max_value=150, step=1)
        sex = st.selectbox("Sex", ["Male", "Female"])
        infection = st.selectbox("Infection", ["No", "Yes"])
        sysbp = st.number_input("SysBP", value=100, min_value=0, max_value=500, step=1)
        pulse = st.number_input("Pulse", value=100, min_value=0, max_value=500, step=1)
        emergency = st.selectbox("Emergency", ["No", "Yes"])
        

        #handle input data
        sex = 0 if sex=='Female' else 1

        agroup = 0
        if age >= 50:
            agroup = 2
        elif age >= 70:
            agroup = 3
        else:
            agroup = 1

        convert_dic = {'Yes':1, 'No':0}
        infection = convert_dic[infection]
        emergency = convert_dic[emergency]

        

        if st.button("Submit"):
            #display result when prompted    
            st.success(model_api('log_reg_model', age, agroup, sex, infection, sysbp, pulse, emergency))

            #saving new record to logging database
            logging(age, agroup, sex, infection, sysbp, pulse, emergency, Id)
    else:

        st.title("This is new patient data input logs")
        st.dataframe(show_logs())
        


    
        

        

if __name__ == "__main__":
    #run with command: streamlit run app.py
    main()