from django.shortcuts import render, redirect
from django.contrib import admin
from django.urls import path, include

def home_view(request):
    return render(request, 'home.html')  # ✅ يعرض الصفحة الرئيسية

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('', home_view, name='home'),  # ✅ رابط الصفحة الرئيسية
]
