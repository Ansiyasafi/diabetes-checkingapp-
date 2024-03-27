import streamlit as st
from sklearn.preprocessing import OrdinalEncoder
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix,accuracy_score
lister=[]
st.title("REGULAR BLOOD SUGAR LEVEL CHECKING FOR DIABETES")

name=st.text_input("Enter your name")
sex=st.radio("Select sex:", ['female', 'male','Other'])
hypertension=st.radio("Select hypertension:", ['having','no'])
heartdisease=st.radio("Select heart disease:", ['yes','no'])
age=st.slider("select your age", 0, 100)
smoking_history=st.selectbox("select the habit of smoking", ['never', 'No Info', 'current', 'former', 'ever', 'not current'])
bmi=st.slider("Enter the bmi value",1,100)
hba1c=st.number_input("Enter the hbaic value",0,10)
bloodsugar=st.slider("Enter the bloodsugar value",30,500)

    #---------------------------------input data--------------
if sex== "female":
    value=0
    lister.append(value)
elif sex=="male":
    value=1  
    lister.append(value)
else:
    value=2
    lister.append(value) 
lister.append(age)    
if hypertension=='having':
    value1=1
    lister.append(value1)
else:
    value1=0 
    lister.append(value1) 
if heartdisease=='yes':
    value2=1
    lister.append(value2)
else:
    value2=0
    lister.append(value2)
if smoking_history=='never':
    value3=4.0
    lister.append(value3) 
elif smoking_history=='No Info' :
    value3=0.0
    lister.append(value3) 
elif  smoking_history=='current':
    value3=1.0
    lister.append(value3) 
elif  smoking_history=='former':
    value3=3.0
    lister.append(value3)
elif smoking_history=='ever':
    value3=2.0
    lister.append(value3)
else :
    value3=5.0
    lister.append(value3)                      


lister.append(bmi)
lister.append(hba1c)
lister.append(bloodsugar) 

         
ansi=np.array([lister]) 
#-----------------------data set and machine training--------------------------

data=pd.read_csv('D:/appfordiabetes/diabetes_prediction_dataset.csv.zip')
encode=OrdinalEncoder()
data.gender=encode.fit_transform(data[["gender"]])
data.gender.unique()

encode1=OrdinalEncoder()
data.smoking_history=encode1.fit_transform(data[["smoking_history"]])
data.smoking_history.unique()

if st.button('confirm'):
    x=data.drop("diabetes",axis=1)
    y=data["diabetes"]

    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)

    from sklearn.tree import DecisionTreeClassifier
    model=DecisionTreeClassifier().fit(x_train,y_train)
    y_pred=model.predict(x_test)
    result=accuracy_score(y_test,y_pred)
    print(result)
    #-------------------------testing the data----------
    ansi_pred=model.predict(ansi)
    print(ansi_pred)
    if ansi_pred==[1]:
        st.write(f'hi {name},sorry you are identified with diabetes and take care of your health')
    else:
        st.write(f'hi {name},keep going with your healthy health care,your result is negative')    

