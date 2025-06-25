#from django.db import models

# Create your models here.

#class CustomUser(models.Model):
 #   username = models.CharField(max_length=150, unique=True)
  #  email = models.EmailField(unique=True)
   # password = models.CharField(max_length=128) # Store hashed password 
    #first_name = models.CharField(max_length=30, blank=True)
    #last_name = models.CharField(max_length=30, blank=True)
    #is_active = models.BooleanField(default=True)
    #is_staff = models.BooleanField(default=False)   
from django.db import models
class ApprovedStudent(models.Model):
    class_categories = [('1-4','classes 1 to 4'),('5-8','classes 5 to 8'),('9-10','classes 9 to 10'),('11-12','classes 11 to 12')]
    admissionNumber = models.CharField(max_length=20,unique=True)
    email=models.EmailField(unique=True)
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)

    classes=models.CharField(max_length=20,choices=class_categories)
    school=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.admissionNumber}-{self.firstName}"
       # return self.admissionNumber

    


