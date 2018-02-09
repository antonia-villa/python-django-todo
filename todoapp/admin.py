from django.contrib import admin

# import models
from .models import Todo
# Register your models here --> with admin panel

admin.site.register(Todo)
