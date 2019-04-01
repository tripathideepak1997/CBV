from django.db import models
from django.urls import reverse

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("create")



class Student(models.Model):
    name = models.CharField(max_length=256)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, related_name='school')

    def __str__(self):
        return self.name
