from django.contrib import admin
from .models import Student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ["stu_id", "name", "marks", "addr", "date_time", "email"]


admin.site.register(Student, StudentAdmin)
