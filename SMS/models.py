from django.db import models

# Create your models here.

class LoginData(models.Model):
    Username = models.CharField(max_length=25)
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=25)
    User = models.CharField(max_length=25,default='User')
    Permission = models.CharField(max_length=25,default='Denied')
    
class BatchData(models.Model):
    BatchName = models.CharField(max_length=25)
    Classes = models.CharField(max_length=255,default=0)
    CaseStudies = models.CharField(max_length=255,default=0)
    MockTests = models.CharField(max_length=255,default=0)
    Interviews = models.CharField(max_length=255,default=0)
    
class StudentData(models.Model):
    BatchName = models.CharField(max_length=25)
    JoiningDate = models.CharField(max_length=25)
    Name = models.CharField(max_length=25)
    Phone = models.CharField(max_length=25)
    Email = models.CharField(max_length=25)
    PG = models.CharField(max_length=25)
    PG_Branch = models.CharField(max_length=25)
    PG_CGPA = models.CharField(max_length=25)
    PG_Year = models.CharField(max_length=25)
    Degree = models.CharField(max_length=25)
    Degree_Branch = models.CharField(max_length=25)
    Degree_CGPA = models.CharField(max_length=25)
    Degree_Year = models.CharField(max_length=25)
    Inter = models.CharField(max_length=25)
    Inter_Branch = models.CharField(max_length=25)
    Inter_CGPA = models.CharField(max_length=25)
    Inter_Year = models.CharField(max_length=25)
    SSC = models.CharField(max_length=25)
    SSC_Branch = models.CharField(max_length=25)
    SSC_CGPA = models.CharField(max_length=25)
    SSC_Year = models.CharField(max_length=25)
    Classes = models.CharField(max_length=255)
    CaseStudies = models.CharField(max_length=255)
    MockTests = models.CharField(max_length=255)
    Interviews = models.CharField(max_length=255)
    Project = models.CharField(max_length=255)
    Feedback = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)
    
class DateData(models.Model):
    BatchDates = models.CharField(max_length=255)
    
class SendOTP(models.Model):
    Email = models.CharField(max_length=255)
    OTP = models.CharField(max_length=255)