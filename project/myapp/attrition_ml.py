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

#Suppress warnings
import warnings
warnings.filterwarnings('ignore')

import pickle
def save_data(fname, classifier):
    with open(fname, 'wb') as picklefile:
        pickle.dump(classifier, picklefile)

def load_data(fname):
    with open(fname, 'rb') as training_model:
        model = pickle.load(training_model)
    return model

def train_test_ml_model(X_train,y_train,X_test,model,Model):
    model.fit(X_train,y_train) #Train the Model
    # y_pred = model.predict(X_test) #Use the Model for prediction

    # # Test the Model
    # from sklearn.metrics import confusion_matrix
    # cm = confusion_matrix(y_test,y_pred)
    # accuracy = round(100*np.trace(cm)/np.sum(cm),1)
    # print('Accuracy of the Model' ,Model, str(accuracy)+'%')
    return model



def train_model(csv_file,model_fname):
    #Import Employee Attrition data
    data=pd.read_csv(csv_file)
    data.head()

    data.info()

    data['Over18'].value_counts()

    data.describe()

    #These fields does not add value, hence removed
    data = data.drop(['EmployeeCount','Over18'], axis = 1)
    # data = data.drop(['BusinessTravel','Department'], axis = 1)
    # data = data.drop(['Education','Gender'], axis = 1)
    # data = data.drop(['MaritalStatus','OverTime'], axis = 1)
    # data = data.drop(['JobRole','EducationField'], axis = 1)

    data['Attrition']=data['Attrition'].apply(lambda x : 1 if x=='Yes' else 0)

    data.head()

    data=pd.get_dummies(data)
    #print(data.head())
    print(data.info())
    print(data.describe())

    X = data.drop(['Attrition'], axis=1)
    y=data['Attrition']

    from sklearn.preprocessing import StandardScaler
    scale = StandardScaler()
    X = scale.fit_transform(X)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size =0.2,random_state=42)




    ##################### SVC #########################
    from sklearn.svm import SVC,NuSVC  #Import packages related to Model
    Model = "SVC"
    model=SVC() #Create the Model

    model = train_test_ml_model(X_train,y_train,X_test,model,Model)
    save_data(f'{model_fname}data_set_svm.model', model)

    ######################### LogisticRegression #################
    Model = 'LogisticRegression'
    model = LogisticRegression()
    model = train_test_ml_model(X_train,y_train,X_test,model,Model)
    save_data(f'{model_fname}data_set_lr.model', model)

    ######################### DecisionTreeClassifier #################
    Model = 'DecisionTreeClassifier'
    model = DecisionTreeClassifier()
    model = train_test_ml_model(X_train,y_train,X_test,model,Model)
    save_data(f'{model_fname}data_set_dtree.model', model)
    
    ######################### RandomForestClassifier #################
    Model = 'RandomForestClassifier'
    model = RandomForestClassifier()
    model = train_test_ml_model(X_train,y_train,X_test,model,Model)
    save_data(f'{model_fname}data_set_forest.model', model)

    # ########################## NuSVC ########################
    # from sklearn.svm import SVC,NuSVC  #Import packages related to Model
    # Model = "NuSVC"
    # model=NuSVC(nu=0.285)#Create the Model

    # train_test_ml_model(X_train,y_train,X_test,Model)

    # ################## xgboost #################
    # from xgboost import XGBClassifier  #Import packages related to Model
    # Model = "XGBClassifier()"
    # model=XGBClassifier() #Create the Model

    # train_test_ml_model(X_train,y_train,X_test,Model)

    # #################### KNN ###################
    # from sklearn.neighbors import KNeighborsClassifier  #Import packages related to Model
    # Model = "KNeighborsClassifier"
    # model=KNeighborsClassifier()

    # train_test_ml_model(X_train,y_train,X_test,Model)


def predict_result(input_set, model_fname):

    # columns = ['Age','BusinessTravel','DailyRate','Department','DistanceFromHome',
    #         'Education','EducationField','EmployeeNumber',
    #         'EnvironmentSatisfaction','Gender','HourlyRate','JobInvolvement',
    #         'JobLevel','JobRole','JobSatisfaction','MaritalStatus','MonthlyIncome',
    #         'MonthlyRate','NumCompaniesWorked','OverTime','PercentSalaryHike',
    #         'PerformanceRating','RelationshipSatisfaction','StandardHours',
    #         'StockOptionLevel','TotalWorkingYears','TrainingTimesLastYear',
    #         'WorkLifeBalance','YearsAtCompany','YearsInCurrentRole',
    #         'YearsSinceLastPromotion','YearsWithCurrManager']
    # df = pd.DataFrame([input_set], columns=columns)
    # #df['BusinessTravel'] = pd.to_numeric(df['BusinessTravel'], errors='coerce').fillna(0.0)
    # from sklearn.preprocessing import StandardScaler
    # scale = StandardScaler()
    # X = scale.fit_transform(df)
    # print(X)
    new_model = load_data(model_fname)
    arr = np.array(input_set)
    y_pred = new_model.predict([input_set])#.reshape(1, -1))
    print(y_pred)
    return y_pred
csv_file='../dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv'
# data_file_path = os.path.join(BASE_DIR, 'data/data_set.csv')
model_file_path = '../dataset/'
#41,Yes,Travel_Rarely,1102,Sales,1,2,Life Sciences,1,1,2,Female,94,3,2,Sales Executive,4,Single,5993,19479,8,Y,Yes,11,3,1,80,0,8,0,1,6,4,0,5
#49,No,Travel_Frequently,279,Research & Development,8,1,Life Sciences,1,2,3,Male,61,2,2,Research Scientist,2,Married,5130,24907,1,Y,No,23,4,4,80,1,10,3,3,10,7,1,7
#Age,Attrition,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,EmployeeCount,EmployeeNumber,EnvironmentSatisfaction,Gender,HourlyRate,JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate,NumCompaniesWorked,Over18,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager
#34,Yes,Travel_Frequently,658,Research & Development,7,3,Life Sciences,1,147,1,Male,66,1,2,Laboratory Technician,3,Single,6074,22887,1,Y,Yes,24,4,4,80,0,9,3,3,9,7,0,6

#22,No,Travel_Rarely,594,Research & Development,2,1,Technical Degree,1,169,3,Male,100,3,1,Laboratory Technician,4,Married,2523,19299,0,Y,No,14,3,3,80,1,3,2,3,2,1,2,1
input = [22,594,2,1,1,169,3,100,3,1,4,2523,19299,0,14,3,3,80,1,3,2,3,2,1,2,1]
#[34,658,7,3,1,147,1,66,1,2,3,6074,22887,1,24,4,4,80,0,9,3,3,9,7,0,6]
#[49,279,8,1,1,2,3,61,2,2,2,5130,24907,1,23,4,4,80,1,10,3,3,10,7,1,7]
#[41,1102,1,2,1,1,2,94,3,2,4,5993,19479,8,11,3,1,80,0,8,0,1,6,4,0,5]

#predict_result(input_set=input, model_fname=model_file_path)
# train_model(csv_file,model_file_path)


#Age,Attrition,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,EmployeeCount,EmployeeNumber,EnvironmentSatisfaction,Gender,HourlyRate,JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate,NumCompaniesWorked,Over18,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager
