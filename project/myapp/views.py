from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import user_login

def index(request):
    return render(request, './myapp/index.html')


def about(request):
    return render(request, './myapp/about.html')


def contact(request):
    return render(request, './myapp/contact.html')

##########################################################################
############################ ADMIN #######################################
def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/admin_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/admin_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/admin_login.html',context)


def admin_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'./myapp/admin_home.html')


def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)

def admin_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['user_name']
        try:
            ul = user_login.objects.get(uname=uname,passwd=opasswd,u_type='admin')
            if ul is not None:
                ul.passwd=npasswd
                ul.save()
                context = {'msg': 'Password Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Err Not Changed'}
            return render(request, './myapp/admin_changepassword.html', context)
    else:
        context = {'msg': ''}
        return render(request, './myapp/admin_changepassword.html', context)

from datetime import datetime
from .models import staff_details
# 2. staff_details - id, user_id ,emp_code, fname ,lname ,gender , designation,addr ,pin ,contact ,email, dt, status

def admin_staff_details_add(request):
    if request.method == 'POST':

        emp_code = request.POST.get('emp_code')
        designation = request.POST.get('designation')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        dt = request.POST.get('dt')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=emp_code
        #status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='staff')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        sd = staff_details(user_id=user_id,emp_code=emp_code, fname=fname, 
                           lname=lname, gender=gender,
                           designation=designation, dt=dt,
                           addr=addr, pin=pin, contact=contact, email=email )
        sd.save()

        print(user_id)
        context = {'msg': 'Staff Registered'}
        return render(request, 'myapp/admin_staff_details_add.html',context)

    else:
        return render(request, 'myapp/admin_staff_details_add.html')

def admin_staff_details_view(request):
    ul_l = user_login.objects.filter(u_type='staff')

    tm_l = []
    for u in ul_l:
        if u.id ==1:
            continue
        sd = staff_details.objects.filter(user_id=u.id).first()
        if sd:
            tm_l.append(sd)
    context = {'staff_list':tm_l,'type':'Staff Details'}
    return render(request, './myapp/admin_staff_details_view.html',context)

# 3. dataset_master - id, Age,Attrition,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,EmployeeCount,EmployeeNumber,EnvironmentSatisfaction,Gender,HourlyRate,JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate,NumCompaniesWorked,Over18,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager
from .models import dataset_master
def admin_dataset_master_add(request):
    if request.method == 'POST':

        Age = request.POST.get('Age')
        Attrition = request.POST.get('Attrition')
        BusinessTravel = request.POST.get('BusinessTravel')
        DailyRate = request.POST.get('DailyRate')

        Department = request.POST.get('Department')
        DistanceFromHome = request.POST.get('DistanceFromHome')
        Education = request.POST.get('Education')
        EducationField = request.POST.get('EducationField')
        EmployeeCount = request.POST.get('EmployeeCount')
        EmployeeNumber = request.POST.get('EmployeeNumber')
        EnvironmentSatisfaction = request.POST.get('EnvironmentSatisfaction')
        Gender = request.POST.get('Gender')
        HourlyRate = request.POST.get('HourlyRate')
        JobInvolvement = request.POST.get('JobInvolvement')
        JobLevel = request.POST.get('JobLevel')
        JobRole = request.POST.get('JobRole')
        JobSatisfaction = request.POST.get('JobSatisfaction')
        MaritalStatus = request.POST.get('MaritalStatus')
        MonthlyIncome = request.POST.get('MonthlyIncome')
        MonthlyRate = request.POST.get('MonthlyRate')
        NumCompaniesWorked = request.POST.get('NumCompaniesWorked')
        Over18 = request.POST.get('Over18')
        OverTime = request.POST.get('OverTime')
        
        PercentSalaryHike = request.POST.get('PercentSalaryHike')
        PerformanceRating = request.POST.get('PerformanceRating')
        RelationshipSatisfaction = request.POST.get('RelationshipSatisfaction')
        StandardHours = request.POST.get('StandardHours')
        StockOptionLevel = request.POST.get('StockOptionLevel')
        
        TotalWorkingYears = request.POST.get('TotalWorkingYears')
        TrainingTimesLastYear = request.POST.get('TrainingTimesLastYear')
        WorkLifeBalance = request.POST.get('WorkLifeBalance')
        YearsAtCompany = request.POST.get('YearsAtCompany')
        YearsInCurrentRole = request.POST.get('YearsInCurrentRole')
        
        YearsSinceLastPromotion = request.POST.get('YearsSinceLastPromotion')
        YearsWithCurrManager = request.POST.get('YearsWithCurrManager')
        
        

        dm_obj = dataset_master(Age=Age,Attrition=Attrition, BusinessTravel=BusinessTravel, 
                           DailyRate=DailyRate, Department=Department,
                           DistanceFromHome=DistanceFromHome, Education=Education,
                           EducationField=EducationField, EmployeeCount=EmployeeCount, 
                           EmployeeNumber=EmployeeNumber, EnvironmentSatisfaction=EnvironmentSatisfaction,
                            Gender=Gender,HourlyRate=HourlyRate, JobInvolvement=JobInvolvement,
                            JobLevel=JobLevel, JobRole=JobRole,  JobSatisfaction=JobSatisfaction,
                            MaritalStatus=MaritalStatus, MonthlyIncome=MonthlyIncome, MonthlyRate=MonthlyRate,
                            NumCompaniesWorked=NumCompaniesWorked, Over18=Over18, OverTime=OverTime,
                            PercentSalaryHike=PercentSalaryHike, PerformanceRating=PerformanceRating, 
                            RelationshipSatisfaction=RelationshipSatisfaction, StandardHours=StandardHours, 
                            StockOptionLevel=StockOptionLevel, TotalWorkingYears=TotalWorkingYears,
                            TrainingTimesLastYear=TrainingTimesLastYear, WorkLifeBalance=WorkLifeBalance,
                            YearsAtCompany=YearsAtCompany,YearsInCurrentRole=YearsInCurrentRole,
                            YearsSinceLastPromotion=YearsSinceLastPromotion, YearsWithCurrManager=YearsWithCurrManager)
        dm_obj.save()

        
        context = {'msg': 'Staff Registered'}
        return render(request, 'myapp/admin_dataset_master_add.html',context)

    else:
        return render(request, 'myapp/admin_dataset_master_add.html')

def admin_dataset_master_view(request):
    dm_l = dataset_master.objects.all()

    context = {'dataset_list':dm_l}
    return render(request, './myapp/admin_dataset_master_view.html',context)

import os
from .attrition_ml import *
from project.settings import BASE_DIR

def admin_dataset_master_train(request):
    #dm_l = dataset_master.objects.all()
    # csv_file='./dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv'
    data_file_path = os.path.join(BASE_DIR, 'dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv')
    model_file_path = os.path.join(BASE_DIR, 'dataset/')
    train_model(data_file_path,model_file_path)
    context = {'msg':'Model Trained'}
    return render(request, './myapp/admin_msg.html',context)

def admin_dataset_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    dm_obj = dataset_master.objects.get(id=int(id))
    dm_obj.delete()

    dm_l = dataset_master.objects.all()

    context = {'dataset_list':dm_l, 'msg':'Record deleted'}
    return render(request, './myapp/admin_dataset_master_view.html',context)

def admin_staff_feedback_view(request):

    nm_l = feedback.objects.all()
    cmd = {}
    for nm in nm_l:
        ud = staff_details.objects.filter(user_id=nm.user_id).first()
        if ud:
            cmd[nm.user_id] = f'{ud.fname} {ud.lname} ({ud.emp_code})'


    context = {'message_list': nm_l, 'user_list': cmd}
    return render(request, 'myapp/admin_staff_feedback_view.html', context)

################################################################################
################################ STAFF ##########################################

from .models import staff_details

def staff_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='staff')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/staff_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/staff_login.html',context)
    else:
        return render(request, 'myapp/staff_login.html')

def staff_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/staff_home.html',context)
    #send_mail("heoo", "hai", 'snehadavisk@gmail.com')

def staff_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/staff_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/staff_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/staff_changepassword.html', context)
    else:
        return render(request, './myapp/staff_changepassword.html')



def staff_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return staff_login_check(request)
    else:
        return staff_login_check(request)

def staff_staff_details_view(request):
    ul_l = user_login.objects.filter(u_type='staff')

    tm_l = []
    for u in ul_l:
        if u.id ==1:
            continue
        sd = staff_details.objects.filter(user_id=u.id).first()
        if sd:
            tm_l.append(sd)
    context = {'staff_list':tm_l,'type':'Staff Details'}
    return render(request, './myapp/staff_staff_details_view.html',context)

from .models import feedback
def staff_feedback_add(request):
    if request.method == 'POST':

        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')

        msg = request.POST.get('msg')

        user_id=int(request.session['user_id'])
        ####################
        km = feedback(user_id=user_id, msg=msg, dt=dt, tm=tm,status='ok')
        km.save()
        context = {'msg': 'feedback posted'}
        return render(request, 'myapp/staff_feedback_add.html', context)
    else:

        context = {}

        return render(request, 'myapp/staff_feedback_add.html',context)

def staff_feedback_delete(request):
    id = request.GET.get('id')
    print("id=" + id)

    nm = feedback.objects.get(id=int(id))
    nm.delete()
    user_id = int(request.session['user_id'])
    nm_l = feedback.objects.filter(user_id=user_id)
    cmd = {}
    for nm in nm_l:
        ud = staff_details.objects.get(user_id=nm.user_id)
        cmd[nm.user_id] = f'{ud.fname} {ud.lname}'

    context = {'message_list': nm_l, 'user_list': cmd,'msg':'Deleted'}
    return render(request, 'myapp/staff_feedback_view.html', context)

def staff_feedback_view(request):
    user_id = int(request.session['user_id'])
    nm_l = feedback.objects.filter(user_id=user_id)
    cmd = {}
    for nm in nm_l:
        ud = staff_details.objects.get(user_id=nm.user_id)
        cmd[nm.user_id] = f'{ud.fname} {ud.lname}'


    context = {'message_list': nm_l, 'user_list': cmd}
    return render(request, 'myapp/staff_feedback_view.html', context)

# 4. query_history - id, user_id, staff_name, emp_code, Age,Attrition,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,EmployeeCount,EmployeeNumber,EnvironmentSatisfaction,Gender,HourlyRate,JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate,NumCompaniesWorked,Over18,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager, dt, tm, result, status
from .models import query_history
from .attrition_ml2 import *
def staff_query_history_add(request):
    if request.method == 'POST':
        user_id = int(request.session['user_id'])
        staff_name = request.POST.get('staff_name')
        emp_code = request.POST.get('emp_code')
        Age = request.POST.get('Age')
        Attrition = 'none'#request.POST.get('Attrition')
        BusinessTravel = request.POST.get('BusinessTravel')
        DailyRate = request.POST.get('DailyRate')

        Department = request.POST.get('Department')
        DistanceFromHome = request.POST.get('DistanceFromHome')
        Education = request.POST.get('Education')
        EducationField = request.POST.get('EducationField')
        EmployeeCount = request.POST.get('EmployeeCount')
        EmployeeNumber = request.POST.get('EmployeeNumber')
        EnvironmentSatisfaction = request.POST.get('EnvironmentSatisfaction')
        Gender = request.POST.get('Gender')
        HourlyRate = request.POST.get('HourlyRate')
        JobInvolvement = request.POST.get('JobInvolvement')
        JobLevel = request.POST.get('JobLevel')
        JobRole = request.POST.get('JobRole')
        JobSatisfaction = request.POST.get('JobSatisfaction')
        MaritalStatus = request.POST.get('MaritalStatus')
        MonthlyIncome = request.POST.get('MonthlyIncome')
        MonthlyRate = request.POST.get('MonthlyRate')
        NumCompaniesWorked = request.POST.get('NumCompaniesWorked')
        Over18 = request.POST.get('Over18')
        OverTime = request.POST.get('OverTime')
        
        PercentSalaryHike = request.POST.get('PercentSalaryHike')
        PerformanceRating = request.POST.get('PerformanceRating')
        RelationshipSatisfaction = request.POST.get('RelationshipSatisfaction')
        StandardHours = request.POST.get('StandardHours')
        StockOptionLevel = request.POST.get('StockOptionLevel')
        
        TotalWorkingYears = request.POST.get('TotalWorkingYears')
        TrainingTimesLastYear = request.POST.get('TrainingTimesLastYear')
        WorkLifeBalance = request.POST.get('WorkLifeBalance')
        YearsAtCompany = request.POST.get('YearsAtCompany')
        YearsInCurrentRole = request.POST.get('YearsInCurrentRole')
        
        YearsSinceLastPromotion = request.POST.get('YearsSinceLastPromotion')
        YearsWithCurrManager = request.POST.get('YearsWithCurrManager')

        # BusinessTravel_d ={'Travel_Rarely':0,'Travel_Frequently':1}
        # Department_d ={'Sales':0,'Travel_Frequently':1}
        # Gender_d ={'Male':0,'Female':1}
        # MaritalStatus_d ={'Married':0,'Divorced':1,'Single':2}
        # OverTime_d={'Yes':0,'No':1}

        input_data = [Age,Attrition,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,EmployeeCount,EmployeeNumber,EnvironmentSatisfaction,Gender,HourlyRate,JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate,NumCompaniesWorked,Over18,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager
]
        data_file_path = os.path.join(BASE_DIR, 'dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv')
        model_file_path = os.path.join(BASE_DIR, 'dataset/data_set_svm.model')
        results = get_prediction(csv_file=data_file_path, input_set=input_data)
        print(results)
        r = {1:'Yes',0:'No'}
        #pr = predict_result(input_set=input_data, model_fname=model_file_path)
        #41,Yes,Travel_Rarely,1102,Sales,1,2,Life Sciences,1,1,2,Female,94,3,2,Sales Executive,4,Single,5993,19479,8,Y,Yes,11,3,1,80,0,8,0,1,6,4,0,5

        
        
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'Yes'
        #"SVC",'LogisticRegression', 'DecisionTreeClassifier','RandomForestClassifier' 
        result = f'''Report :
        SVC: {r[results[0]]}, LogisticRegression: {r[results[1]]}, DecisionTreeClassifier: {r[results[2]]}, RandomForestClassifier: {r[results[3]]}'''
        

        qh_obj = query_history(
            user_id=user_id, staff_name=staff_name, emp_code=emp_code,
            Age=Age,Attrition=Attrition, BusinessTravel=BusinessTravel, 
            DailyRate=DailyRate, Department=Department,
            DistanceFromHome=DistanceFromHome, Education=Education,
            EducationField=EducationField, EmployeeCount=EmployeeCount, 
            EmployeeNumber=EmployeeNumber, EnvironmentSatisfaction=EnvironmentSatisfaction,
            Gender=Gender,HourlyRate=HourlyRate, JobInvolvement=JobInvolvement,
            JobLevel=JobLevel, JobRole=JobRole,  JobSatisfaction=JobSatisfaction,
            MaritalStatus=MaritalStatus, MonthlyIncome=MonthlyIncome, MonthlyRate=MonthlyRate,
            NumCompaniesWorked=NumCompaniesWorked, Over18=Over18, OverTime=OverTime,
            PercentSalaryHike=PercentSalaryHike, PerformanceRating=PerformanceRating, 
            RelationshipSatisfaction=RelationshipSatisfaction, StandardHours=StandardHours, 
            StockOptionLevel=StockOptionLevel, TotalWorkingYears=TotalWorkingYears,
            TrainingTimesLastYear=TrainingTimesLastYear, WorkLifeBalance=WorkLifeBalance,
            YearsAtCompany=YearsAtCompany,YearsInCurrentRole=YearsInCurrentRole,
            YearsSinceLastPromotion=YearsSinceLastPromotion, YearsWithCurrManager=YearsWithCurrManager,
            dt=dt, tm=tm, result=result, status=status)
        qh_obj.save()
        
        context = {'msg': result}
        return render(request, 'myapp/staff_query_history_add.html',context)

    else:
        return render(request, 'myapp/staff_query_history_add.html')

def staff_query_history_view(request):
    user_id = int(request.session['user_id'])
    dm_l = query_history.objects.filter(user_id=user_id)

    context = {'dataset_list':dm_l}
    return render(request, './myapp/staff_query_history_view.html',context)

# def admin_dataset_master_delete(request):
#     id = request.GET.get('id')
#     print("id="+id)

#     dm_obj = dataset_master.objects.get(id=int(id))
#     dm_obj.delete()

#     dm_l = dataset_master.objects.all()

#     context = {'dataset_list':dm_l, 'msg':'Record deleted'}
#     return render(request, './myapp/admin_dataset_master_view.html',context)


################################################################################
############################### USER UNUSED ###############################################
from .models import user_details

def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='user')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/user_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/user_login.html',context)
    else:
        return render(request, 'myapp/user_login.html')

def user_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/user_home.html',context)
    #send_mail("heoo", "hai", 'snehadavisk@gmail.com')

def user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        age = request.POST.get('age')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=email
        #status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='user')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname, gender=gender, age=age,addr=addr, pin=pin, contact=contact, email=email )
        ud.save()

        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/user_login.html',context)

    else:
        return render(request, 'myapp/user_details_add.html')

def user_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/user_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/user_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/user_changepassword.html', context)
    else:
        return render(request, './myapp/user_changepassword.html')



def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)



