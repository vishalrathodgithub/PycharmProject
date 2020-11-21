from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .models import Student
from .forms import StudentForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Student_View(LoginRequiredMixin, View):
    login_url = "/login/"
    template_name = "app/stu.html"

    def get(self, request):
        data = Student.objects.all()
        return render(request, self.template_name, context={"data": data})


class Class_Base_View(View):
    form = StudentForm
    template_name = "app/temp.html"

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, context={"form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            user = request.POST["name"]
            messages.info(request, f'user added successful for user {user}')
            return redirect("/stu/")
        return render(request, self.template_name, context={"form": form})


class Delete_Student(View):

    def get(self, request, id):
        del_stu = Student.objects.get(stu_id=id)
        del_stu.delete()
        messages.info(request, f'user deleted successfully for user {del_stu.name}')
        return redirect("/stu/")


class Update_Student(View):
    template_name = "app/update.html"

    def get(self, request, id):
        stu_data = Student.objects.get(stu_id=id)
        form = StudentForm(instance=stu_data)
        return render(request, self.template_name, context={"form": form})

    def post(self, request, id):
        stu_data = Student.objects.get(stu_id=id)
        if request.method == "POST":
            form = StudentForm(request.POST, instance=stu_data)
            if form.is_valid():
                form.save()
                messages.info(request, f'update user successful for user {stu_data.name}')
                return redirect("/stu/")
        return render(request, self.template_name, context={"form": form})

