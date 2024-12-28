from django.db import models
from .choices import QUESTION_CHOICES
from django.contrib.auth.models import User
# Create your models here.
class BaseModel(models.Model):
    createdAt : models.DateField(auto_now_add=True)
    updatedAt : models.DateField(auto_now=True)
    
    class Meta:
        abstract = True
        
class Choices(BaseModel):
    choice = models.CharField(max_length=200)
    
class Question(BaseModel):
    question : models.CharField(max_length=200)
    question_type = models.CharField(max_length=200,choices=QUESTION_CHOICES)
    required = models.BooleanField(default=True)
    choices = models.ManyToManyField(Choices,related_name="question_choices",blank=True)

class Form(BaseModel):
    code = models.CharField(max_length=200,unique=True)
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question,related_name="questions")
    
    
    