from django.contrib import admin

# Register your models here.
# usersapp/admin.py
from django.contrib import admin
from .models import Todo  # Ensure the model is correctly imported

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'due_date')  # Customize as needed
