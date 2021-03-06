from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AiClass(models.Model):
    class_num = models.IntegerField()
    lecturer = models.CharField(max_length=10)
    class_room_num = models.CharField(max_length=10)
    

class AiStudent(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='student')
    
    participate_class = models.ForeignKey(
        AiClass, on_delete=models.CASCADE, related_name='student')
    
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=5)
    phone_num = models.CharField(max_length=30)
    

class StudentPost(models.Model):
    writer = models.ForeignKey(
        AiStudent, on_delete=models.SET_NULL, null=True, related_name='post')
    intro = models.TextField()

    