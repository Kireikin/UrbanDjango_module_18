from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister  # ContactForm,


def sign_up_by_html(request):
    if request.method == "POST":
        # Получаем данные:
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        print(f'username: {username}')
        print(f'password: {password}')
        print(f'repeat_password: {repeat_password}')
        print(f'age: {age}')
        # Http ответ пользователю:
        check = True
        return HttpResponse(f"Приветствуем, '{username}'!", check)
        # если это  GET запрос:
    return render(request, 'fifth_task/registration_page.html')


def sign_up_by_django(request):
    if request.method == "POST":
        # Получаем данные:
        form = UserRegister(request.POST)
        if form.is_valid():
            # обработка данных
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            # Тут дальнейшая логика например отправка емайла
            print(f'username: {username}')
            print(f'password: {password}')
            print(f'repeat_password: {repeat_password}')
            print(f'age: {age}')
            return HttpResponse(f"Приветствуем, '{username}'!")
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', {'form': form})


def choose(request):
    return render(request, 'fifth_task/choose.html')


# def index(request):
#     if request.method == "POST":
#         # Получаем данные:
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         subscribe = request.POST.get('subscribe') == 'on'
#
#         print(f'Name: {name}')
#         print(f'email: {email}')
#         print(f'message: {message}')
#         print(f'subscribe: {subscribe}')
#
#         # Http ответ пользователю:
#         return HttpResponse("Форма успешно отправлена")
#     # если это  GET запрос:
#     return render(request, 'fifth_task/copy_lection_html.html')


# def index(request):
#     if request.method == "POST":
#         # Получаем данные:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # обработка данных
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             subscribe = form.cleaned_data['subscribe']
#             # Тут дальнейшая логика например отправка емайла
#             print(f'Name: {name}')
#             print(f'email: {email}')
#             print(f'message: {message}')
#             print(f'subscribe: {subscribe}')
#             return HttpResponse("Форма успешно отправлена")
#     else:
#         form = ContactForm()
#     return render(request, 'fifth_task/copy_lection_html.html', {'form': form})
