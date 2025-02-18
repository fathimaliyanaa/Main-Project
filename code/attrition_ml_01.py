##Importing the packages
#Data processing packages
import numpy as np 
import pandas as pd 

#Visualization packages
import matplotlib.pyplot as plt 
import seaborn as sns 

#Machine Learning packages
from sklearn.svm import SVC,NuSVC
# from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB,MultinomialNB
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis, LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler	
from sklearn.metrics import confusion_matrix

#Suppress warnings
import warnings
warnings.filterwarnings('ignore')

#Import Employee Attrition data
data=pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
data.head()

data.info()

data['Over18'].value_counts()

data.describe()

#These fields does not add value, hence removed
data = data.drop(['EmployeeCount','Over18'], axis = 1)

data['Attrition']=data['Attrition'].apply(lambda x : 1 if x=='Yes' else 0)

data.head()

data=pd.get_dummies(data)
data.head()

X = data.drop(['Attrition'], axis=1)
y=data['Attrition']

from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
X = scale.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size =0.2,random_state=42)

def train_test_ml_model(X_train,y_train,X_test,Model):
    model.fit(X_train,y_train) #Train the Model
    y_pred = model.predict(X_test) #Use the Model for prediction

    # Test the Model
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test,y_pred)
    accuracy = round(100*np.trace(cm)/np.sum(cm),1)

    #Plot/Display the results
    # cm_plot(cm,Model)
    print('Accuracy of the Model' ,Model, str(accuracy)+'%')

from sklearn.svm import SVC,NuSVC  #Import packages related to Model
Model = "SVC"
model=SVC() #Create the Model

train_test_ml_model(X_train,y_train,X_test,Model)

import pickle

filename = 'model.dat'
pickle.dump(model,open(filename, 'wb'))
