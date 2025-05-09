from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class Department(models.Model):
    dept_name = models.CharField(max_length=20)
    city =  models.CharField(max_length=30)

    def __str__(self):
        return f"{self.dept_name}"



class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    birth_date = models.DateField()
    notes = models.CharField(max_length=200)
    country= models.ForeignKey(Country,on_delete=models.CASCADE),
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
