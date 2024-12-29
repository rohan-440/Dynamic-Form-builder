from rest_framework import serializers
from .models import Question,Form,Responses,Choices,ResponseAnswer





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
                "question_id" : question.id,
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
  

class ResponseAnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = ResponseAnswer
        fields = '__all__'
        
        def to_representation(self,instance):
            data = {
                "answer" : instance.answer,
                "answer_to" : {
                    "question" : instance.answer_to.question,
                    "question_type" : instance.answer_to.question,
                }
            }
            return data
            
    
class ResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responses
        exclude = ["createdAt","updatedAt","creator","id"]
    
    def to_representation(self, instance):
        data = {
            "id" : instance.id,
            "code" : instance.code,
            "responder_email" : instance.responder_email,
            "form" : {
              "code" : instance.form.code,
              "title" : instance.form.title ,
            },
            "responses" : ResponseAnswerSerializers(instance.responses.all(),many = True).data
            
        }
        return data