from django.contrib import admin
from .models import Employee_Type,Employee,User,Feedback,Query,Offers_Scheme,User_Feedback,User_Query

class Emptype_Admin(admin.ModelAdmin):
    list_display=('employee_type','charge_permonth')
    list_filter=['charge_permonth']
    search_fields=('employee_type',)

class Employee_Admin(admin.ModelAdmin):
    list_display=('name','phone','email','employee_type','gender','experience')
    search_fields=('name',)

class User_Admin(admin.ModelAdmin):
    list_display=('userid','name','email','phone','address')
    list_filter=['name']
    search_fields=('userid',)

class Feedback_Admin(admin.ModelAdmin):
    list_display=('name','email','rating')
    list_filter=['rating']
    search_fields=('name',)
 
class Query_Admin(admin.ModelAdmin):
    list_display=('name','email','phone')
    search_fields=('name',)

class Offer_Admin(admin.ModelAdmin):
    list_display=('offercontents',)




# Register your models here.
admin.site.register(Employee_Type,Emptype_Admin)
admin.site.register(Employee,Employee_Admin)
admin.site.register(User,User_Admin)
admin.site.register(Feedback,Feedback_Admin)
admin.site.register(Query,Query_Admin)
admin.site.register(Offers_Scheme,Offer_Admin)
admin.site.register(User_Feedback)
admin.site.register(User_Query)



admin.site.site_header="Safe Home Solutions Adminstration"
admin.site.site_title="Safe Home Admin Dashboard"
admin.site.index_title="Admin"
