"""
URL configuration for teamtask project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # هذا يجعل `/` يذهب إلى تطبيق `tasks`
]
