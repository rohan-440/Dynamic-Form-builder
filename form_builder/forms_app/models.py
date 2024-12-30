from django.db import models
from .choices import QUESTION_CHOICES
from django.contrib.auth.models import User
from .utils import generate_random_code



#base model for time 
class BaseModel(models.Model):
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True
        
        
# choice model like text,drop down,check box    
class Choices(BaseModel):
    choice = models.CharField(max_length=200)
    def __str__(self):
        return self.choice
    
    
    
#Question model
class Question(BaseModel):
    question = models.CharField(max_length=200)
    question_type = models.CharField(max_length=200,choices=QUESTION_CHOICES)
    required = models.BooleanField(default=True)
    choices = models.ManyToManyField(Choices,related_name="question_choices",blank=True)
    def __str__(self):
        return self.question



#Form model
class Form(BaseModel):
    code = models.CharField(max_length=200,unique=True,blank=True)
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question,related_name="questions")
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if not self.pk:
           self.code = generate_random_code(9).lower()  #get random code 
        super(Form,self).save(*args,**kwargs)
    



class ResponseAnswer(BaseModel):
    answer = models.CharField(max_length=200)
    answer_to = models.ForeignKey(Question,on_delete=models.CASCADE,related_name="answer_to")
    def __str__(self):
        return self.answer


#Response form
class Responses(BaseModel):
    code  = models.CharField(max_length=200,unique=True,blank=True)
    form = models.ForeignKey(Form,on_delete=models.CASCADE,related_name="forms")
    responder_email = models.CharField(max_length=200,null=True,blank=True)
    responses = models.ManyToManyField(ResponseAnswer)
    def save(self,*args,**kwargs):
        if not self.pk:
            self.code = generate_random_code(9).lower() #save the response on that particular code 
        super(Responses,self).save(*args,**kwargs)
    # def __str__(self):
    #     return self.responses   
    
    