from django.shortcuts import render
from django.urls import reverse_lazy

from .models import School,Student
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.


class SchoolList(View):

    def get(self, request):
        objects = School.objects.all()
        print(objects)
        return render(request, 'file1.html', {'objects': objects})


class StudentList(View):

    def get(self, request):
        objects = Student.objects.all()
        return render(request, 'file1.html', {'objects': objects})


class StudentListListView(ListView):
    model = Student
    context_object_name = 'objects'
    template_name = 'file1.html'


class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'objects'
    template_name = 'file2.html'


class SchoolCreateView(CreateView):
    model = School
    fields = ['name', ]
    template_name = 'school_form.html'


class SchoolUpdateView(UpdateView):
    model = School
    fields = ['name', ]
    template_name = 'school_form.html'


class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('school')
    template_name = 'delete_form.html'
