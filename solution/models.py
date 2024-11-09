from django.db import models
from django.utils import timezone

# Create your models here.
gender=[
    ("M","Male"),
    ("F","Female")
]

class Employee_Type(models.Model):
    employee_type=models.CharField(max_length=45,primary_key=True)
    charge_permonth=models.IntegerField()
    other_details=models.TextField()

    def __str__(self):
        return self.employee_type

class Employee(models.Model):
    name=models.CharField(max_length=45)
    phone=models.CharField(max_length=10)
    address=models.TextField()
    email=models.EmailField(max_length=45)
    age=models.IntegerField()
    gender=models.CharField(max_length=6,choices=gender)
    experience=models.CharField(max_length=20)
    employee_pic=models.FileField(max_length=100,upload_to="solution/employee_pic",default="")
    employee_type=models.ForeignKey(Employee_Type,on_delete=models.CASCADE)
    about_employee=models.TextField()
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
    
class User(models.Model):
    userid=models.CharField(max_length=45)
    userpass=models.CharField(max_length=45)
    name=models.CharField(max_length=45)
    phone=models.CharField(max_length=10)
    address=models.TextField()
    email=models.EmailField(max_length=45)
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.name

class Feedback(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45)
    date=models.DateField(default=timezone.now)
    feedback_text=models.TextField()
    rating=models.IntegerField()
    def __str__(self):
        return self.name
    
class Query(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45)
    phone=models.CharField(max_length=10)
    question=models.TextField()
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.name

class Offers_Scheme(models.Model):
    offercontents=models.CharField(max_length=45)
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.offercontents
    
class User_Feedback(models.Model):
    user=models.OneToOneField(User,on_delete=models.DO_NOTHING)
    feedback_text=models.TextField()
    rating=models.CharField(max_length=6)
    date=models.DateField(default=timezone.now)

class User_Query(models.Model):
    user=models.OneToOneField(User,on_delete=models.DO_NOTHING) 
    question=models.TextField()
    date=models.DateField(default=timezone.now)

    


    