from django.db import models

# Create your models here.
class classes(models.Model):
    class_num = models.IntegerField()
    lecturer = models.CharField(max_length=10)
    class_room = models.CharField(max_length=10)
    students_num = models.IntegerField()

    
class AiStudents(models.Model):
    studentID = models.IntegerField()
    name = models.CharField(max_length=10)
    class_num = models.IntegerField()
    sex = models.CharField(max_length=2)
    phone_number = models.CharField(max_length=30)
    major = models.CharField(max_length=30)
    

