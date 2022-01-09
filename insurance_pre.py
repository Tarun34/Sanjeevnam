import streamlit as st
import insurance
st.set_page_config(page_title="Sanjeevnam",
                   layout="wide",
                   page_icon="downloa.png")
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">',unsafe_allow_html=True)
st.markdown("""
     <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color:#3498DB;">
     <a class="navbar-brand fa fa-stethoscope" style="font-size:30px" href="http://localhost:8501/" target="_blank"> Sanjeevnam </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="http://localhost:8501/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:8502/" target="_blank"> Vaccine </a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:8503/" target="_blank">Disease</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:8504/" target="_blank">Health Insurance</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)
insurance.app()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# loading the data from csv file to a Pandas DataFrame
insurance_dataset = pd.read_csv('./insurance1.csv')

    # first 5 rows of the dataframe
insurance_dataset.head()

    # number of rows and columns

    # getting some informations about the dataset
insurance_dataset.info()
    # checking for missing values
insurance_dataset.isnull().sum()

    # statistical Measures of the dataset
insurance_dataset.describe()

    # distribution of age value
# sns.set()
# plt.figure(figsize=(6, 6))
# sns.distplot(insurance_dataset['age'])
# plt.title('Age Distribution')
# plt.show()
#
#     # Gender column
# plt.figure(figsize=(6, 6))
# sns.countplot(x='sex', data=insurance_dataset)
# plt.title('Sex Distribution')
# plt.show()
#
# insurance_dataset['sex'].value_counts()
#
#     # bmi distribution
# plt.figure(figsize=(6, 6))
# sns.distplot(insurance_dataset['bmi'])
# plt.title('BMI Distribution')
# plt.show()
#     # children column
# plt.figure(figsize=(6, 6))
# sns.countplot(x='children', data=insurance_dataset)
# plt.title('Children')
# plt.show()
#
# insurance_dataset['children'].value_counts()
#
#     # smoker column
# plt.figure(figsize=(6, 6))
# sns.countplot(x='smoker', data=insurance_dataset)
# plt.title('smoker')
# plt.show()
#
# insurance_dataset['smoker'].value_counts()
#
#     # region column
# plt.figure(figsize=(6, 6))
# sns.countplot(x='region', data=insurance_dataset)
# plt.title('region')
# plt.show()
#
# insurance_dataset['region'].value_counts()
#
#     # distribution of charges value
# plt.figure(figsize=(6, 6))
# sns.distplot(insurance_dataset['charges'])
# plt.title('Charges Distribution')
# plt.show()
    # encoding sex column
insurance_dataset.replace({'sex': {'male': 0, 'female': 1}}, inplace=True)

  # encoding 'smoker' column
insurance_dataset.replace({'smoker': {'yes': 0, 'no': 1}}, inplace=True)

    # encoding 'region' column
insurance_dataset.replace({'region': {'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}},
                              inplace=True)

X = insurance_dataset.drop(columns='charges', axis=1)
Y = insurance_dataset['charges']

print(X)

print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)
    # loading the Linear Regression model
regressor = LinearRegression()

regressor.fit(X_train, Y_train)

    # prediction on training data
training_data_prediction = regressor.predict(X_train)

    # R squared value
r2_train = metrics.r2_score(Y_train, training_data_prediction)
print('R squared vale : ', r2_train)

    # prediction on test data
test_data_prediction = regressor.predict(X_test)

    # R squared value
r2_test = metrics.r2_score(Y_test, test_data_prediction)
print('R squared vale : ', r2_test)
with st.form(key='my_form'):
        st.markdown("<h1 style='text-align:justify; font-family:Cursive;'><b><center> Insurance Cost Predictor </center></b></h1>",unsafe_allow_html=True)
        c1 = st.number_input("age")
        c2 = st.number_input("sex")
        c3 = st.number_input("bmi")
        c4 = st.number_input("children")
        c5 = st.number_input("smoker")
        c6 = st.number_input("region")

        input_data = (c1, c2, c3, c4, c5, c6)

        # changing input_data to a numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the array
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

        prediction = regressor.predict(input_data_reshaped)
        if st.form_submit_button("Predict"):
            st.write('The insurance cost is Ruppes ', prediction[0]*70)