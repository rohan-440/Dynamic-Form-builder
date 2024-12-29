from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question,Form,Responses,ResponseAnswer,Choices
from .serializers import QuestionSerializer,FormSerializer,ResponseAnswerSerializers,ResponsesSerializer
from django.db import transaction
# Create your views here.



class QuestionAPI(APIView):
    def get(self,request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset,many =True)
        return Response({
            "status" :  True,
            "message" : "questions fetched successfully",
            "data" : serializer.data
        })
        
        
class FormAPI(APIView):
    def get(self,request,pk):
        queryset = Form.objects.get(code=pk)
        serializer = FormSerializer(queryset)
        return Response({
            "status" : True,
            "message" : "Form fetched successfully",
            "data" : serializer.data
        })
        
  
  
  
  
class FormResponseAPI(APIView):
    def get(self,request,pk):
        queryset = Responses.objects.filter(form__code = pk)
        serializer = ResponsesSerializer(queryset,many = True)
        return Response({
            "status" : True,
            "message" : "Form fetched successfully",
            "data" : serializer.data
        })  
  
  
        
        
        
class StoreResponseAPI(APIView):
    def post(self,request):
        data = request.data
        with transaction.atomic():
            if data.get('form_code') is None or data.get('responses') is None:
                return Response({
                "status" : False,
                "message" : "something went wrong",
                "data" : {}
                    
                })
            responses = data.get('responses')
            response_obj = Responses.objects.create(
                form = Form.objects.get(code = data.get('form_code') )
            )
            
            for response in responses:
                question = Question.objects.get(id = response['question_id'])
                for answer in response['answers']:
                    if question.question_type in ["Text"]:
                        answer_obj = ResponseAnswer.objects.create(
                            answer = answer,
                            answer_to = question
                        )
                    else :
                        answer_obj = ResponseAnswer.objects.create(
                            answer = Choices.objects.get(id = answer),
                            answer_to = question
                        )
                    response_obj.responses.add(answer_obj)
            
            return Response({
                "status" : True,
                "message" : "Your response has been submitted",
                "data" : {}
            })
        