import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score
import streamlit as st

def app():
    parkinsons_data = pd.read_csv('./parkinsons.csv')
    # printing the first 5 rows of the dataframe
    parkinsons_data.head()
    # number of rows and columns in the dataframe
    parkinsons_data.shape
    # getting more information about the dataset
    parkinsons_data.info()
    # checking for missing values in each column
    parkinsons_data.isnull().sum()
    # getting some statistical measures about the data
    parkinsons_data.describe()
    # distribution of target Variable
    parkinsons_data['status'].value_counts()
    # grouping the data bas3ed on the target variable
    parkinsons_data.groupby('status').mean()

    X = parkinsons_data.drop(columns=['name','status'], axis=1)
    Y = parkinsons_data['status']
    print(X)
    print(Y)
    #Splitting the data to training data & Test data
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
    print(X.shape, X_train.shape, X_test.shape)
    #Data Standardization
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)

    X_test = scaler.transform(X_test)
    print(X_train)
    #Model Training
    #Support Vector Machine Model
    model = svm.SVC(kernel='linear')
    # training the SVM model with training data
    model.fit(X_train, Y_train)
    #Model Evaluation
    #Accuracy Score
    # accuracy score on training data
    X_train_prediction = model.predict(X_train)
    training_data_accuracy = accuracy_score(Y_train, X_train_prediction)
    print('Accuracy score of training data : ', training_data_accuracy)
    # accuracy score on training data
    X_test_prediction = model.predict(X_test)
    test_data_accuracy = accuracy_score(Y_test, X_test_prediction)
    print('Accuracy score of test data : ', test_data_accuracy)
    #Building a Predictive System

    st.markdown("<h1 style='text-align:justify; color:red; font-family:archia;'><center> Parkinson Disease</center> </h1>",unsafe_allow_html=True)
    col2, col3, col4 = st.columns([17,17,1])
    with col2:
        a= st.number_input('MDVP:Fo(Hz)')
        b=st.number_input('MDVP:Fhi(Hz)')
        c=st.number_input(' MDVP:Flo(Hz) ')
        d= st.number_input(' MDVP:Jitter(%)  ')
        e= st.number_input('  MDVP:Jitter(Abs)')
    with col3:
       f= st.number_input(' MDVP:RAP ')
       g = st.number_input('MDVP:PPQ')
       h= st.number_input(' Jitter:DDP ')
       i= st.number_input('MDVP:Shimmer ')
       j= st.number_input(" MDVP:Shimmer(dB)")

    add_button=st.sidebar.button('results ')
    input_data = (a,b,c,d,e,f,g,h,i,j,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)
    # changing input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the numpy array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # standardize the data
    std_data = scaler.transform(input_data_reshaped)

    prediction = model.predict(std_data)
    print(prediction)


    if (prediction[0] == 0):
        st.text("The Person does not have Parkinsons Disease")


    else:
        print("The Person has Parkinsons")





