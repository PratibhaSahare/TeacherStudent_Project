from django.db import models

# Create your models here.

class Teacher(models.Model):

    emp_id= models.IntegerField()
    first_name= models.CharField(max_length=30,default="unknown")
    last_name= models.CharField(max_length=50)
    age= models.IntegerField()
    blood_group= models.CharField(max_length=3,null=True)
    is_marrital=models.BooleanField()
    email_id=models.EmailField()
    address=models.CharField(max_length=200)
    job_profile=models.CharField(max_length=50)


    def _str_(self):
        return self.first_name
       




