import pandas as pd
import numpy as np
import pickle
import streamlit as st

df_model = pd.read_csv('data_perusahaan.csv')
loaded_model = pickle.load(open(model_predictive_updated.sav, 'rb'))

# Creating a function for prediction
def attrition_prediction(input):

    data_as_array = np.asarray(input)
    reshaped = data_as_array.reshape(1,-1)
    prediction = loaded_model.predict(reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
        return 'does not contain attrition'
    else:
        return 'contains attrition'

def main():
    # giving a tittle
    st.title('Attrition Prediction Web App')

    # getting input the data from user
    age = st.text_input('Number of Age')
    business_travel = st.text_input('Number of Business Travel (KM)')
    education_field = st.text_input('Number of Education Field Category')
    environment_satisfaction = st.text_input('Number of Environment Satisfaction Level')
    job_involvement = st.text_input('Number of Job Involvement Level')
    job_role = st.text_input('Number of Job Role')
    job_satisfaction = st.text_input('Number of Job Satisfaction Level')
    marital_status = st.text_input('Number of Marital Status Category')
    monthly_income = st.text_input('Number of Monthly_Income')
    monthly_rate = st.text_input('Number of Monthly Rate')
    over_time = st.text_input('Number of Over Time Category')
    stock_option_level = st.text_input('Number of Stock Option level')
    years_in_current_role = st.text_input('Number of Years in Current Role')
    years_since_last_promotion = st.text_input('Number of Years Since Last Promotion')
    years_with_curr_manager = st.text_input('Number of Years With Current Manager')

    # Code for predictions
    prediction = ''

    # Creating a button for prediction
    if st.button('Prediction test Result'):
        prediction = attrition_prediction([age, business_travel, education_field, environment_satisfaction, job_involvement, job_role, job_satisfaction, marital_status, monthly_income, monthly_rate, over_time, stock_option_level, years_in_current_role, years_since_last_promotion, years_with_curr_manager])
    st.success(prediction)

if __name__ == '__main__':
    main()
