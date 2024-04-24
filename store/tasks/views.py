from django.http import HttpResponse
from django.urls import reverse

def index(request):
    another_page_url = reverse('tasks:another_page')
    quality_control_page_url = reverse('quality_control:main')
    html = (f"<h1>Страница приложения tasks</h1>"
            f"<a href='{another_page_url}'>Перейти на другую страницу<br></a>"
            f"<a href='{quality_control_page_url}'>Перейти на страницу приложения quality_control<br></a>")
    return HttpResponse(html)

def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")