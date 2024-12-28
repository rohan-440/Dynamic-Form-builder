from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .serializers import QuestionSerializer

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