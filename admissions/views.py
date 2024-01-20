from django.shortcuts import render
from admissions.models import student, Teachersmodel  # Class based views
from admissions.forms import studentmodelform
from admissions.forms import vendorform
# For class based views
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
# Create your views here.


def homepage(request):
    return render(request, "index.html")


def newadmission(request):
    x = studentmodelform
    x_dic = {"form": x}

    if request.method == 'POST':
        form = studentmodelform(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)

    return render(request, "admissions/newadmission.html", x_dic)


def admissionreport(request):
    # First Fetch all the data from Models for this we will use object method and store in a variable.
    result = student.objects.all()  # It is same as SQL Query " Select * From Students"
    # Now we have to create a Dictionary & Assign it to it
    # Assigning in a dictionary format in key value pairs
    students = {"Allstudents": result}
    return render(request, "admissions/admissionreport.html", students)


def addvendor(request):
    x = vendorform
    x_dic = {"form": x}

    if request.method == 'POST':
        form = vendorform(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['address'])
            print(form.cleaned_data['contact'])
            print(form.cleaned_data['item'])
        return homepage(request)

    return render(request, "admissions/addvendor.html", x_dic)


# performing CRUD Opertaions, In this fucntion we will delete the user given Idvalue
def deletedata(request, id):
    s = student.objects.get(id=id)
    s.delete()
    return admissionreport(request)


def updatedata(request, id):
    s = student.objects.get(id=id)
    form = studentmodelform(instance=s)
    dic = {"form": form}

    if request.method == 'POST':
        form = studentmodelform(request.POST, instance=s)
        if form.is_valid():
            form.save()
        return admissionreport(request)

    return render(request, "admissions/updateadmission.html", dic)


# class based views
class firstclassbasedview(View):
    def get(self, request):
        return HttpResponse("This is Class based view")

# creating TEachers report.


class Teachersreport(ListView):
    model = Teachersmodel

# creating or retreving Single object


class Teacherdetails(DetailView):
    model = Teachersmodel

# creating form using classes


class addteacher(CreateView):
    model = Teachersmodel
    fields = ('name', 'subject', 'exp', 'contact')

# updating infomration


class UpdateTeacher(UpdateView):
    model = Teachersmodel
    fields = ('name', 'contact')


class removeteacher(DeleteView):
    model = Teachersmodel
    success_url = reverse_lazy('listteachers')
