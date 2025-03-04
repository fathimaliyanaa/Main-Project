##Importing the packages
#Data processing packages
import numpy as np 
import pandas as pd 

#Visualization packages
import matplotlib.pyplot as plt 
import seaborn as sns 

#Machine Learning packages
from sklearn.svm import SVC,NuSVC
#from xgboost import XGBClassifier
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

def get_prediction(csv_file, input_set):
    #Suppress warnings
    import warnings
    warnings.filterwarnings('ignore')

    #Import Employee Attrition data
    data=pd.read_csv(csv_file)#'./dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv')
    data.loc[len(data)] = input_set
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
    print(len(X),'*****************',X[1469])

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size =0.2,random_state=42)

    def train_test_ml_model(X_train,y_train,X_test,Model):
        model.fit(X_train,y_train) #Train the Model
        y_pred = model.predict([X[len(X)-1]]) #Use the Model for prediction
        print(y_pred)
        return y_pred
        # Test the Model
        # from sklearn.metrics import confusion_matrix
        # cm = confusion_matrix(y_test,y_pred)
        # accuracy = round(100*np.trace(cm)/np.sum(cm),1)

        # #Plot/Display the results
        # cm_plot(cm,Model)
        # print('Accuracy of the Model' ,Model, str(accuracy)+'%')



    results = []
    ##################### SVC #########################
    from sklearn.svm import SVC,NuSVC  #Import packages related to Model
    Model = "SVC"
    model=SVC() #Create the Model

    r1 = train_test_ml_model(X_train,y_train,X_test,Model)

    ######################### LogisticRegression #################
    Model = 'LogisticRegression'
    model = LogisticRegression()
    r2 = train_test_ml_model(X_train,y_train,X_test,Model)

    ######################### DecisionTreeClassifier #################
    Model = 'DecisionTreeClassifier'
    model = DecisionTreeClassifier()
    r3 = train_test_ml_model(X_train,y_train,X_test,Model)
    
    ######################### RandomForestClassifier #################
    Model = 'RandomForestClassifier'
    model = RandomForestClassifier()
    r4 = train_test_ml_model(X_train,y_train,X_test,Model)



    # ########################## NuSVC ########################
    # from sklearn.svm import SVC,NuSVC  #Import packages related to Model
    # Model = "NuSVC"
    # model=NuSVC(nu=0.285)#Create the Model

    # r2 = train_test_ml_model(X_train,y_train,X_test,Model)

    # ################## xgboost #################
    # from xgboost import XGBClassifier  #Import packages related to Model
    # Model = "XGBClassifier()"
    # model=XGBClassifier() #Create the Model

    # r3 = train_test_ml_model(X_train,y_train,X_test,Model)

    # #################### KNN ###################
    # from sklearn.neighbors import KNeighborsClassifier  #Import packages related to Model
    # Model = "KNeighborsClassifier"
    # model=KNeighborsClassifier()

    # r4 = train_test_ml_model(X_train,y_train,X_test,Model)

    results = [int(r1[0]),int(r2[0]), int(r3[0]), int(r4[0])]
    return results

# csv_file='../dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv'
# input_set = [41,'Yes','Travel_Rarely',1102,'Sales',1,2,'Life Sciences',
#              1,1,2,'Female',94,3,2,'Sales Executive',4,'Single',
#              5993,19479,8,'Y','Yes',11,3,1,80,0,8,0,1,6,4,0,5]
# results = get_prediction(csv_file=csv_file, input_set=input_set)
# print(results)