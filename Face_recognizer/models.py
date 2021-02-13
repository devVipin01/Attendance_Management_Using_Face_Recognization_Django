from django.db import models

# Create your models here.
class MyData(models.Model):
    Student= models.CharField(max_length=30,blank=False)
    Date_Time = models.DateTimeField(blank=False,auto_now=True)
    #time = models.TimeField(blank=False,auto_now=True)
    #attendence = models.BooleanField(blank=False, default=False)

    #def __str__(self):
        #return self.Student
    
     
    
