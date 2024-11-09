from .models import Offers_Scheme,Employee,Employee_Type,Feedback,Query
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):
    offer_list=Offers_Scheme.objects.all().order_by('-date')
    employee_type_list=Employee_Type.objects.all()
    offer_context={
        "offer_key":offer_list,
        "emptype":employee_type_list
    }
    return render(request,"solution/html/index.html",offer_context)

def show_emp(request,emp_type):
    
    emp_type_obj=Employee_Type.objects.get(employee_type=emp_type)
    employee_list=Employee.objects.filter(employee_type=emp_type_obj)
    employee_dict={

        "emp_data":employee_list
    }
    return render(request,"solution/html/showemp.html",employee_dict)

def employee(request):
    emp_type=Employee_Type.objects.all()
    emp_type_dict={
        "emp_data":emp_type
    }
    return render(request,'solution/html/employee_type.html',emp_type_dict)

def feedback(request):
    if request.method=="GET":
        return render(request,'solution/html/feedback.html')
    if request.method=="POST":
        u_name=request.POST["username"]
        u_email=request.POST["useremail"]
        u_feedback=request.POST["userfeedback"]
        u_rating=request.POST["userrating"]
        uf=Feedback(name=u_name,email=u_email,feedback_text=u_feedback,rating=u_rating)
        uf.save()
        messages.success(request,"Thankyou so much for your valuable feedback.")
        return render(request,'solution/html/feedback.html')
    
def query(request):
    if request.method=="GET":
        return render(request,'solution/html/query.html')
    if request.method=="POST":
        u_name=request.POST["username"]
        u_email=request.POST["useremail"]
        u_phone=request.POST["userphone"]
        u_query=request.POST["userquery"]
        uq=Query(name=u_name,email=u_email,phone=u_phone,question=u_query)
        uq.save()
        messages.success(request,"Thankyou for inquiring with us. We will get back to you..")
        return render(request,'solution/html/query.html')
    
def about_us(request):
    return render(request,'solution/html/about_us.html')

def contact_us(request):
    return render(request,'solution/html/contact_us.html')
