from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500)

    def __str__(self) -> str:
        return f"{self.name}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"


