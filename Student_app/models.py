from django.db import models

# Create your models here.

class Student(models.Model):

    roll_number= models.IntegerField()
    first_name= models.CharField(max_length=30,default="unknown")
    last_name= models.CharField(max_length=50)
    age= models.IntegerField()
    blood_group= models.CharField(max_length=3,null=True)


    def _str_(self):
        return self.first_name

