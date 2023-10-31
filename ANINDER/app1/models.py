from django.db import models

# Create your models here.
class login(models.Model):
    Mobile_Number = models.TextField(max_length=13)
    Latitude=models.FloatField()
    Longitude=models.FloatField()
class forest_department_login(models.Model):
    Name = models.TextField(max_length=30)
    Division = models.TextField(max_length=30)
    Designation = models.TextField(max_length=30)
    Email = models.EmailField()
class camera(models.Model):
    CAM_ID = models.TextField(max_length=15)
    Animal=models.TextField(max_length=30)
    Datetime=models.TextField(max_length=30)
class suggestions(models.Model):
    Name=models.TextField(max_length=30)
    Designation=models.TextField(max_length=30)
    Email=models.TextField(max_length=30)
    suggestions=models.TextField(max_length=500)
class report_intrusion(models.Model):
    Animal=models.TextField(max_length=30)
    Location=models.TextField(max_length=30)
    Date_and_Time=models.TextField(max_length=30)
class add_camera_location(models.Model):
      CAM_ID=models.TextField(max_length=15)
      Location=models.TextField(max_length=30)
      latitude=models.FloatField()
      longitude=models.FloatField()


