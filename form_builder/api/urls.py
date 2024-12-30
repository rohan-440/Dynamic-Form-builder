from django.urls import path,include
from forms_app.views import QuestionAPI,FormAPI,StoreResponseAPI,FormResponseAPI

urlpatterns = [
    
    path('questions/',QuestionAPI.as_view()), # url for set of questions
    path('form/<pk>/',FormAPI.as_view()),   # url for to get form
    path('store-response/',StoreResponseAPI.as_view()),  # url for storing response
    path('form/responses/<pk>/',FormResponseAPI.as_view()), # url to see the response of form 
]
