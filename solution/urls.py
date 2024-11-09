from django.urls import path
from .import views,user_views
urlpatterns =[
    path("",views.index,name="index"),
    path("registration/",user_views.registration,name="registration"),
    path("login/",user_views.login,name="login"),    
    path("user_home/",user_views.user_home,name="user_home"),  
    path("logout/",user_views.logout,name="logout"),  
    path("user_edit_profile/",user_views.update,name="edit_profile"),  
    path("user_feedback/",user_views.feedback,name="feedback"),
    path("user_query/",user_views.query,name="query"),
    path("ouremployee/",views.employee,name="employee"),
    path("showemp/<str:emp_type>/",views.show_emp,name="show_emp"),
    path("feedback/",views.feedback,name="feedback"),
    path("query/",views.query,name="query"),
    path("about/",views.about_us,name="about_us"),
    path("contact/",views.contact_us,name="contact_us"),
        ]  