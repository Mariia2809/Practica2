from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import UserProfile, Category, Request

def home(request):
    # Представление для главной страницы
    return render(request, 'home.html')

def login_view(request):
    # Представление для авторизации
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Редирект на личный кабинет
    return render(request, 'login.html')

def registration(request):
    # Представление для регистрации
    if request.method == 'POST':
    # Обработка данных регистрации
        # Создание нового пользователя
        # Редирект на авторизацию
    return render(request, 'registration.html')

    def user_dashboard(request):
    # Представление для личного кабинета авторизованного пользователя
        # Вывод заявок пользователя
    return render(request, 'user_dashboard.html', context)

    def admin_dashboard(request):
    # Представление для личного кабинета администратора
        # Вывод заявок и управление категориями
    return render(request, 'admin_dashboard.html', context)