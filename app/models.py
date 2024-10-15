from django.db import models

# Create your models here.

#        terminal admin

class terminal_admin(models.Model):
    id=models.CharField(primary_key=True, max_length=30)
    name=models.CharField(max_length=30)
    contact=models.BigIntegerField()
    email=models.EmailField(max_length=30)
    iterm=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

#      driver admin
class Driver_Data(models.Model):
    id=models.CharField(primary_key=True, max_length=30)
    name=models.CharField(max_length=30)
    contact=models.BigIntegerField()
    email=models.EmailField(max_length=30)
    busno=models.CharField(max_length=10)
    iterm=models.CharField(max_length=30)
    fterm=models.CharField(max_length=30)
    date=models.DateField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    goingtime=models.TimeField()
    reachtime=models.TimeField(null=True,blank=True)
    leavetime=models.TimeField(null=True,blank=True)
    finaltime=models.TimeField(null=True,blank=True)

#     attendence
class atend(models.Model):
    uid=models.CharField(max_length=30,null=True)
    name=models.CharField(max_length=30)
    name_p=models.CharField(max_length=10, null=True)  #see
    busno=models.CharField(max_length=10)
    bus_p=models.CharField(max_length=10, null=True)  #see
    iterm=models.CharField(max_length=30)
    fterm=models.CharField(max_length=30)
    date=models.DateField()
    goingtime=models.TimeField()
    reachtime=models.TimeField(null=True,blank=True)
    leavetime=models.TimeField(null=True,blank=True)
    finaltime=models.TimeField(null=True,blank=True)
    
    
