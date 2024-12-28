from rest_framework import serializers
from .models import Question,Form

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ["createdAt","updatedAt"]


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        exclude = ["createdAt","updatedAt","creator","id"]
    
    def to_representation(self, instance):
        questions = []
        
        for question in instance.questions.all():
            choices = None
            if question.question_type in ["Dropdown","Checkbox"]:
                choices = []
                for choice in question.choices.all():
                    choices.append({"id" : choice.id, "choice" : choice.choice})
            questions.append({
                "question" : question.question,
                "question_type"  :question.question_type,
                "required": question.required,
                "choices" : choices
            })
            
            data = {
                "id" : question.id,
                "code" : instance.code,
                "title" : instance.title,
                "questions" : questions,
            }
            
        return data