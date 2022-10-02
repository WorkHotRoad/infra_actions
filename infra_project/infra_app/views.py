from django.http import HttpResponse


def index(request):
    return HttpResponse('Ура, всё работает')


def second_page(request):
    return HttpResponse('А это вторая страница!')
