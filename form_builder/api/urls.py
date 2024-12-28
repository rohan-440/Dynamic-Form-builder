from django.urls import path,include
from forms_app.views import QuestionAPI,FormAPI

urlpatterns = [
    path('questions/',QuestionAPI.as_view()),
    path('form/<pk>/',FormAPI.as_view()),
]
