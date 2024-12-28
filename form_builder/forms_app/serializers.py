from rest_framework import serializers
from .models import Question,Form

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ["createdAt","updatedAt"]


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        exclude = ["createdAt","updatedAt"]