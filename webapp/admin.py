from django.contrib import admin
from .models import Emp

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ['id','Eid','Ename','Eloc','Eadd']
admin.site.register(Emp,EmpAdmin)
# this rajkumar
