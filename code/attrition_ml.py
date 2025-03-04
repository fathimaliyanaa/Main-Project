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

#Import Employee Attrition data
data=pd.read_csv('./dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv')
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

    #########################################################
    from sklearn.metrics import f1_score, recall_score, roc_curve, roc_auc_score
    # Calculate F1 score
    f1 = f1_score(y_test, y_pred) 
    print("F1 Score:", f1)

    # Calculate recall
    recall = recall_score(y_test, y_pred) 
    print("Recall:", recall)

    if Model != 'DecisionTreeClassifier' and Model != 'RandomForestClassifier':
        # Calculate ROC curve
        fpr, tpr, thresholds = roc_curve(y_test, model.decision_function(X_test))  # Use decision_function for SVM 

    if Model != 'DecisionTreeClassifier' and Model != 'RandomForestClassifier':
    
        # Calculate AUC-ROC
        roc_auc = roc_auc_score(y_test, model.decision_function(X_test)) 
        print("AUC-ROC:", roc_auc)
        roc_plot(fpr, tpr,roc_auc)
    ##########################################################
    # Test the Model
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test,y_pred)
    accuracy = round(100*np.trace(cm)/np.sum(cm),1)

    #Plot/Display the results
    cm_plot(cm,Model)
    print('Accuracy of the Model' ,Model, str(accuracy)+'%')


#Function to plot Confusion Matrix
def cm_plot(cm,Model):
    plt.clf()
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Wistia)
    classNames = ['Negative','Positive']
    plt.title('Comparison of Prediction Result for '+ Model)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    tick_marks = np.arange(len(classNames))
    plt.xticks(tick_marks, classNames, rotation=45)
    plt.yticks(tick_marks, classNames)
    s = [['TN','FP'], ['FN', 'TP']]
    for i in range(2):
        for j in range(2):
            plt.text(j,i, str(s[i][j])+" = "+str(cm[i][j]))
    plt.show()

def roc_plot(fpr, tpr, roc_auc):
    plt.title('Receiver Operating Characteristic')
    plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
    plt.legend(loc = 'lower right')
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()
##################### SVC #########################
from sklearn.svm import SVC,NuSVC  #Import packages related to Model
Model = "SVC"
model=SVC() #Create the Model

train_test_ml_model(X_train,y_train,X_test,Model)

########################## NuSVC ########################
from sklearn.svm import SVC,NuSVC  #Import packages related to Model
Model = "NuSVC"
model=NuSVC(nu=0.285)#Create the Model

train_test_ml_model(X_train,y_train,X_test,Model)

######################### LogisticRegression #################
Model = 'LogisticRegression'
model = LogisticRegression()
train_test_ml_model(X_train,y_train,X_test,Model)

######################### DecisionTreeClassifier #################
Model = 'DecisionTreeClassifier'
model = DecisionTreeClassifier()
train_test_ml_model(X_train,y_train,X_test,Model)
    
######################### RandomForestClassifier #################
Model = 'RandomForestClassifier'
model = RandomForestClassifier()
train_test_ml_model(X_train,y_train,X_test,Model)

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