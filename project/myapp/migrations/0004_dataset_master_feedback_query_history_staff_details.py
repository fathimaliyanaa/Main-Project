# Generated by Django 4.0 on 2025-01-13 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_user_details_kcno'),
    ]

    operations = [
        migrations.CreateModel(
            name='dataset_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.CharField(max_length=100)),
                ('Attrition', models.CharField(max_length=100)),
                ('BusinessTravel', models.CharField(max_length=200)),
                ('DailyRate', models.CharField(max_length=200)),
                ('Department', models.CharField(max_length=200)),
                ('DistanceFromHome', models.CharField(max_length=200)),
                ('Education', models.CharField(max_length=200)),
                ('EducationField', models.CharField(max_length=200)),
                ('EmployeeCount', models.CharField(max_length=200)),
                ('EmployeeNumber', models.CharField(max_length=200)),
                ('EnvironmentSatisfaction', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=100)),
                ('HourlyRate', models.CharField(max_length=100)),
                ('JobInvolvement', models.CharField(max_length=200)),
                ('JobLevel', models.CharField(max_length=100)),
                ('JobRole', models.CharField(max_length=100)),
                ('JobSatisfaction', models.CharField(max_length=200)),
                ('MaritalStatus', models.CharField(max_length=100)),
                ('MonthlyIncome', models.CharField(max_length=100)),
                ('MonthlyRate', models.CharField(max_length=100)),
                ('NumCompaniesWorked', models.CharField(max_length=100)),
                ('Over18', models.CharField(max_length=100)),
                ('OverTime', models.CharField(max_length=100)),
                ('PercentSalaryHike', models.CharField(max_length=100)),
                ('PerformanceRating', models.CharField(max_length=100)),
                ('RelationshipSatisfaction', models.CharField(max_length=100)),
                ('StandardHours', models.CharField(max_length=100)),
                ('StockOptionLevel', models.CharField(max_length=100)),
                ('TotalWorkingYears', models.CharField(max_length=100)),
                ('TrainingTimesLastYear', models.CharField(max_length=100)),
                ('WorkLifeBalance', models.CharField(max_length=100)),
                ('YearsAtCompany', models.CharField(max_length=100)),
                ('YearsInCurrentRole', models.CharField(max_length=100)),
                ('YearsSinceLastPromotion', models.CharField(max_length=100)),
                ('YearsWithCurrManager', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('msg', models.CharField(max_length=500)),
                ('dt', models.CharField(max_length=100)),
                ('tm', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='query_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('staff_name', models.CharField(max_length=100)),
                ('emp_code', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
                ('Attrition', models.CharField(max_length=100)),
                ('BusinessTravel', models.CharField(max_length=200)),
                ('DailyRate', models.CharField(max_length=200)),
                ('Department', models.CharField(max_length=200)),
                ('DistanceFromHome', models.CharField(max_length=200)),
                ('Education', models.CharField(max_length=200)),
                ('EducationField', models.CharField(max_length=200)),
                ('EmployeeCount', models.CharField(max_length=200)),
                ('EmployeeNumber', models.CharField(max_length=200)),
                ('EnvironmentSatisfaction', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=100)),
                ('HourlyRate', models.CharField(max_length=100)),
                ('JobInvolvement', models.CharField(max_length=200)),
                ('JobLevel', models.CharField(max_length=100)),
                ('JobRole', models.CharField(max_length=100)),
                ('JobSatisfaction', models.CharField(max_length=200)),
                ('MaritalStatus', models.CharField(max_length=100)),
                ('MonthlyIncome', models.CharField(max_length=100)),
                ('MonthlyRate', models.CharField(max_length=100)),
                ('NumCompaniesWorked', models.CharField(max_length=100)),
                ('Over18', models.CharField(max_length=100)),
                ('OverTime', models.CharField(max_length=100)),
                ('PercentSalaryHike', models.CharField(max_length=100)),
                ('PerformanceRating', models.CharField(max_length=100)),
                ('RelationshipSatisfaction', models.CharField(max_length=100)),
                ('StandardHours', models.CharField(max_length=100)),
                ('StockOptionLevel', models.CharField(max_length=100)),
                ('TotalWorkingYears', models.CharField(max_length=100)),
                ('TrainingTimesLastYear', models.CharField(max_length=100)),
                ('WorkLifeBalance', models.CharField(max_length=100)),
                ('YearsAtCompany', models.CharField(max_length=100)),
                ('YearsInCurrentRole', models.CharField(max_length=100)),
                ('YearsSinceLastPromotion', models.CharField(max_length=100)),
                ('YearsWithCurrManager', models.CharField(max_length=100)),
                ('dt', models.CharField(max_length=100)),
                ('tm', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='staff_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('emp_code', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=50)),
                ('addr', models.CharField(max_length=600)),
                ('pin', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=150)),
                ('dt', models.CharField(max_length=25)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
