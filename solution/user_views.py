from django.shortcuts import render,redirect
from .models import User,User_Feedback,User_Query,Employee
from django.contrib import messages
from .import views

# Create your views here.
def registration(request):
    if request.method=="GET":
        return render(request,"solution/user/user_registration.html")
    if request.method=="POST":
        id=request.POST["userid"] 
        password=request.POST["userpassword"] 
        name=request.POST["username"]   
        phone=request.POST["userphone"] 
        address=request.POST["useraddress"]
        email=request.POST["useremail"]
        user_obj=User(userid=id,userpass=password,name=name,phone=phone,address=address,email=email)
        user_obj.save()
        messages.success(request,"Congratutations!! You have registered successfully.")
        return render(request,"solution/user/user_registration.html")
       
def login(request):
    if request.method=='GET':
        return render(request,'solution/user/user_login.html')
    if request.method=='POST':
        u_id=request.POST["userid"]
        u_pass=request.POST["userpassword"]
        user_list=User.objects.filter(userid=u_id,userpass=u_pass) 
        if user_list:
            request.session["user_key"]=u_id 
            return redirect("user_home")
        else:
            messages.error(request,"Invalid Credentials.")
            return render(request,"solution/user/user_login.html")
        
def user_home(request):
        if request.method=="GET":
            user_id=request.session["user_key"]
            user_obj=User.objects.get(userid=user_id) 
            user_dict={"user_data":user_obj}  
            return render(request,'solution/user/user_home.html',user_dict)
        if request.method=="POST":
            e_typ=request.POST["selectemp"] 
            user_id=request.session["user_key"]
            user_obj=User.objects.get(userid=user_id) 
            user_dict={"user_data":user_obj}

            
            if e_typ=="1":
                m_list=Employee.objects.filter(employee_type="Maid")
                m_context={
                    "m_key":m_list
                        }
                return render(request,'solution/html/maid.html',{'context1':user_dict,'context2':m_context})
           
            if e_typ=="2":
                g_list=Employee.objects.filter(employee_type="Gardener")
                g_context={
                    "g_key":g_list
                        }
                return render(request,'solution/html/gardener.html',{'context1':user_dict,'context2':g_context})
            
            if e_typ=="3":
                lm_list=Employee.objects.filter(employee_type="Laundary man")
                lm_context={
                    "lm_key":lm_list
                        }
                return render(request,'solution/html/laundaryman.html',{'context1':user_dict,'context2':lm_context})
            
            if e_typ=="4":
                n_list=Employee.objects.filter(employee_type="Nanny")
                n_context={
                    "n_key":n_list
                        }
                return render(request,'solution/html/nanny.html',{'context1':user_dict,'context2':n_context})
            
            if e_typ=="5":
                ct_list=Employee.objects.filter(employee_type="Caretaker")
                ct_context={
                    "ct_key":ct_list
                        }
                return render(request,'solution/html/caretaker.html',{'context1':user_dict,'context2':ct_context})
           
            if e_typ=="6":
                c_list=Employee.objects.filter(employee_type="Cook")
                c_context={
                    "c_key":c_list
                        }
                return render(request,'solution/html/cook.html',{'context1':user_dict,'context2':c_context})
            
            if e_typ=="7":
                s_list=Employee.objects.filter(employee_type="Sweeper")
                s_context={
                    "s_key":s_list
                        }
                return render(request,'solution/html/sweeper.html',{'context1':user_dict,'context2':s_context})
            if e_typ=="8":
                dw_list=Employee.objects.filter(employee_type="Dishwasher")
                dw_context={
                    "dw_key":dw_list
                        }
                return render(request,'solution/html/dishwasher.html',{'context1':user_dict,'context2':dw_context})
          
            if e_typ=="9":
                i_list=Employee.objects.filter(employee_type="Ironer")
                i_context={
                    "i_key":i_list
                        }
                return render(request,'solution/html/ironer.html',{'context1':user_dict,'context2':i_context})
            
                

        

def logout(request):
    del request.session["user_key"]
    return redirect("login")

def update(request):
    if request.method=="GET":
        user_id=request.session["user_key"]
        user_obj=User.objects.get(userid=user_id)
        user_dict={"user_data":user_obj}
        return render(request,'solution/user/user_update.html',user_dict)
    if request.method=="POST":
        u_phone=request.POST["userphone"]
        u_add=request.POST["useraddress"]
        u_email=request.POST["useremail"]
        u_id=request.session["user_key"]
        user_obj=User.objects.get(userid=u_id)
        user_obj.email=u_email
        user_obj.phone=u_phone
        user_obj.address=u_add
        user_obj.save()
        user_dict={"user_data":user_obj}
        return render(request,'solution/user/user_home.html',user_dict)
    
def feedback(request):
    if request.method=="GET":
        u_id=request.session["user_key"]
        user_obj=User.objects.get(userid=u_id)
        user_dict={"user_data":user_obj}
        return render(request,'solution/user/user_feedback.html',user_dict)
    if request.method=="POST":
        u_feedback=request.POST["userfeedback"]
        u_rating=request.POST["userrating"]
        u_id=request.session["user_key"]
        user_obj=User.objects.get(userid=u_id)
        user_object_list=User_Feedback.objects.filter(user_id=user_obj)
        if user_object_list:  
            u_dict={"user_data":user_obj}
            messages.info(request,"You have already given feedback")
            return render(request,'solution/user/user_home.html',u_dict)
        else:
            uf=User_Feedback(user=user_obj,feedback_text=u_feedback,rating=u_rating)
            uf.save()
            u_dict={"user_data":user_obj}
            messages.success(request,"Thankyou so much for your valuable feedback.")
            return render(request,'solution/user/user_home.html',u_dict)

def query(request):
    if request.method=="GET":
        u_id=request.session["user_key"]
        user_obj=User.objects.get(userid=u_id)
        user_dict={"user_data":user_obj}
        return render(request,'solution/user/user_query.html',user_dict)
    if request.method=="POST":
        u_query=request.POST["userquery"]
        u_id=request.session["user_key"]
        user_obj=User.objects.get(userid=u_id)
        uq=User_Query(user=user_obj,question=u_query)
        uq.save()
        u_dict={"user_data":user_obj}
        messages.success(request,"Thankyou for inquiring with us. We will get back to you..")
        return render(request,'solution/user/user_home.html',u_dict)