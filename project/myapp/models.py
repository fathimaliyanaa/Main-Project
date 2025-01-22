from django.db import models

# 1. user_login - id, uname ,passwd ,u_type
# 2. staff_details - id, user_id ,emp_code, fname ,lname ,gender , designation,addr ,pin ,contact ,email, dt, status
# 3. dataset_master - id, Age,Attrition,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,EmployeeCount,EmployeeNumber,EnvironmentSatisfaction,Gender,HourlyRate,JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate,NumCompaniesWorked,Over18,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager
# 4. query_history - id, user_id, staff_name, emp_code, Age,Attrition,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,EmployeeCount,EmployeeNumber,EnvironmentSatisfaction,Gender,HourlyRate,JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate,NumCompaniesWorked,Over18,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager, dt, tm, result, status
# 5. feedback - id, user_id, msg, dt, tm, status




# Create your models here.
# 1. user_login - id, uname ,passwd ,u_type
class user_login(models.Model):
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

    def __str__(self):
        return self.uname

class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=25)
    age = models.IntegerField()
    addr = models.CharField(max_length=500)
    pin = models.IntegerField()
    contact = models.IntegerField()
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.fname


# 2. staff_details - id, user_id ,emp_code, fname ,lname ,gender , designation,addr ,pin ,contact ,email, dt, status
class staff_details(models.Model):
    # id
    user_id = models.IntegerField()
    emp_code = models.CharField(max_length=20) 
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    addr = models.CharField(max_length=600)
    pin = models.CharField(max_length=10) 
    contact = models.CharField(max_length=15)
    email = models.CharField(max_length=150)
    dt = models.CharField(max_length=25)
    status = models.CharField(max_length=20)

# 3. dataset_master - id, Age,Attrition,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,EmployeeCount,EmployeeNumber,EnvironmentSatisfaction,Gender,HourlyRate,JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate,NumCompaniesWorked,Over18,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager
class dataset_master(models.Model):
    #id
    Age = models.CharField(max_length=100)
    Attrition = models.CharField(max_length=100)
    BusinessTravel = models.CharField(max_length=200)
    DailyRate = models.CharField(max_length=200)
    Department = models.CharField(max_length=200)
    DistanceFromHome = models.CharField(max_length=200)
    Education = models.CharField(max_length=200)
    EducationField = models.CharField(max_length=200)
    EmployeeCount = models.CharField(max_length=200)
    EmployeeNumber = models.CharField(max_length=200)
    EnvironmentSatisfaction = models.CharField(max_length=200)
    Gender = models.CharField(max_length=100)
    HourlyRate = models.CharField(max_length=100)
    JobInvolvement = models.CharField(max_length=200)
    JobLevel = models.CharField(max_length=100)
    JobRole = models.CharField(max_length=100)
    JobSatisfaction = models.CharField(max_length=200)
    MaritalStatus = models.CharField(max_length=100)
    MonthlyIncome = models.CharField(max_length=100)
    MonthlyRate = models.CharField(max_length=100)
    NumCompaniesWorked = models.CharField(max_length=100)
    Over18 = models.CharField(max_length=100)
    OverTime = models.CharField(max_length=100)
    PercentSalaryHike = models.CharField(max_length=100)
    PerformanceRating = models.CharField(max_length=100)
    RelationshipSatisfaction = models.CharField(max_length=100)
    StandardHours = models.CharField(max_length=100)
    StockOptionLevel = models.CharField(max_length=100)
    TotalWorkingYears = models.CharField(max_length=100)
    TrainingTimesLastYear = models.CharField(max_length=100)
    WorkLifeBalance = models.CharField(max_length=100)
    YearsAtCompany = models.CharField(max_length=100)
    YearsInCurrentRole = models.CharField(max_length=100)
    YearsSinceLastPromotion = models.CharField(max_length=100)
    YearsWithCurrManager = models.CharField(max_length=100)

# 4. query_history - id, user_id, staff_name, emp_code, Age,Attrition,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,EmployeeCount,EmployeeNumber,EnvironmentSatisfaction,Gender,HourlyRate,JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate,NumCompaniesWorked,Over18,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager, dt, tm, result, status
class query_history(models.Model):
    #id
    user_id = models.IntegerField()
    staff_name = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    Attrition = models.CharField(max_length=100)
    BusinessTravel = models.CharField(max_length=200)
    DailyRate = models.CharField(max_length=200)
    Department = models.CharField(max_length=200)
    DistanceFromHome = models.CharField(max_length=200)
    Education = models.CharField(max_length=200)
    EducationField = models.CharField(max_length=200)
    EmployeeCount = models.CharField(max_length=200)
    EmployeeNumber = models.CharField(max_length=200)
    EnvironmentSatisfaction = models.CharField(max_length=200)
    Gender = models.CharField(max_length=100)
    HourlyRate = models.CharField(max_length=100)
    JobInvolvement = models.CharField(max_length=200)
    JobLevel = models.CharField(max_length=100)
    JobRole = models.CharField(max_length=100)
    JobSatisfaction = models.CharField(max_length=200)
    MaritalStatus = models.CharField(max_length=100)
    MonthlyIncome = models.CharField(max_length=100)
    MonthlyRate = models.CharField(max_length=100)
    NumCompaniesWorked = models.CharField(max_length=100)
    Over18 = models.CharField(max_length=100)
    OverTime = models.CharField(max_length=100)
    PercentSalaryHike = models.CharField(max_length=100)
    PerformanceRating = models.CharField(max_length=100)
    RelationshipSatisfaction = models.CharField(max_length=100)
    StandardHours = models.CharField(max_length=100)
    StockOptionLevel = models.CharField(max_length=100)
    TotalWorkingYears = models.CharField(max_length=100)
    TrainingTimesLastYear = models.CharField(max_length=100)
    WorkLifeBalance = models.CharField(max_length=100)
    YearsAtCompany = models.CharField(max_length=100)
    YearsInCurrentRole = models.CharField(max_length=100)
    YearsSinceLastPromotion = models.CharField(max_length=100)
    YearsWithCurrManager = models.CharField(max_length=100)
    dt = models.CharField(max_length=100)
    tm = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

# 5. feedback - id, user_id, msg, dt, tm, status
class feedback(models.Model):
    #id
    user_id = models.IntegerField()
    msg = models.CharField(max_length=500)
    dt = models.CharField(max_length=100)
    tm = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
