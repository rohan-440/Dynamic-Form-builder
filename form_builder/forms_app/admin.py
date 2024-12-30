from django.contrib import admin
from .models import (Choices,Question,Form,ResponseAnswer,Responses)

# Register the models

admin.site.register(Choices)
admin.site.register(Question)
admin.site.register(Form)
admin.site.register(Responses)
admin.site.register(ResponseAnswer)