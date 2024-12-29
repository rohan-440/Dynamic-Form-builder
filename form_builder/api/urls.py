from django.urls import path,include
from forms_app.views import QuestionAPI,FormAPI,StoreResponseAPI,FormResponseAPI

urlpatterns = [
    path('questions/',QuestionAPI.as_view()),
    path('form/<pk>/',FormAPI.as_view()),
    path('store-response/',StoreResponseAPI.as_view()),
    path('form/responses/<pk>/',FormResponseAPI.as_view()),
]
