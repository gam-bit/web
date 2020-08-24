from django.db import models

# Create your models here.
class AiClass(models.Model):
    class_num = models.IntegerField()
    lecturer = models.CharField(max_length=10)
    class_room_num = models.CharField(max_length=10)
    

class AiStudent(models.Model):
    class_num = models.IntegerField()
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=5)
    phone_num = models.CharField(max_length=30)


    