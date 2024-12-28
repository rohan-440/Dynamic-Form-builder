from django.contrib import admin
from .models import (Choices,Question,Form)

# Register your models here.
admin.site.register(Choices)
admin.site.register(Question)
admin.site.register(Form)