from django.urls import path,include
from forms_app.views import QuestionAPI

urlpatterns = [
    path('questions/',QuestionAPI.as_view())
]
