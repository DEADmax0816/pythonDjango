import django.db.utils
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .my_utils.utils import table_model


def index(request):
    form = UsersForm(request.POST or None)

    if request.method == 'GET':
        context = {
            'form': form
        }
        return render(request, 'main/index.html', context)

    if form.is_valid():
        fio = form.cleaned_data.get('text_fio')
        phone = form.cleaned_data.get('text_phone')
        country = form.cleaned_data.get('text_country')
        city = form.cleaned_data.get('text_city')
        city_index = form.cleaned_data.get('text_city_index')
        place = form.cleaned_data.get('text_place')

        if not Countries.objects.filter(country=place).exists():
            return redirect('country-error')

        new_user = Users(fio=fio, phone=phone, country=country, city=city, city_index=city_index)

        try:
            new_user.save()
        except django.db.utils.IntegrityError:
            return HttpResponse('<h1>Пользователь с таким номером уже существует</h1>')

        new_ticket = Tickets(
            user=new_user,
            country=Countries.objects.get(country=place)
        )
        new_ticket.save()

        return HttpResponse("<h1>Данные отправлены успешно</h1>"
                            "<a href = '/'>Назад</a>")
    else:
        return HttpResponse('<h1>Форма невалидна</h1>')


def country_error(request):
    return HttpResponse("<h1>Страны, в которую вы хотите отправиться, нет в списке</h1>"
                        "<a href = '/'>Назад</a>")


def countries(request):
    counties_list = Countries.objects.values_list('country', flat=True)
    counties_str = ', '.join(counties_list)

    return HttpResponse(f"<h1>{counties_str}</h1>"
                        f"<a href = '/'>Назад</a>")


def tables(request):
    return render(request, 'main/tables.html')


def table_users(request):
    users_str = table_model(Users)
    return HttpResponse(f"<body style='font-family: monospace'>"
                        f"<h2>{users_str}</h2>"
                        f"<a href = '/tables'>Назад</a></body>")


def table_tickets(request):
    tickets_str = table_model(Tickets)
    return HttpResponse(f"<body style='font-family: monospace'>"
                        f"<h2>{tickets_str}</h2>"
                        f"<a href = '/tables'>Назад</a></body>")


def select(request):
    users_query = Users.objects.all()
    select_list = []
    for user in users_query:
        select_list.append((user.id, user.to_string()))

    context = {
        'select_list': select_list
    }

    return render(request, 'main/select.html', context)


def update(request, id):
    try:
        user = Users.objects.get(id=id)
        form = UpdateUserForm(initial={
            'update_fio': user.fio,
            'update_phone': user.phone,
            'update_country': user.country,
            'update_city': user.city,
            'update_city_index': user.city_index
        })
    except Users.DoesNotExist:
        return HttpResponse("<h2>Такого пользователя нет в таблице</h2>")

    if request.method == 'GET':
        context = {
            'form': form
        }
        return render(request, 'main/update.html', context)

    form = UpdateUserForm(request.POST or None)
    if form.is_valid():
        new_fio = form.cleaned_data.get('update_fio')
        new_phone = form.cleaned_data.get('update_phone')
        new_country = form.cleaned_data.get('update_country')
        new_city = form.cleaned_data.get('update_city')
        new_city_index = form.cleaned_data.get('update_city_index')
        user.fio = new_fio
        user.phone = new_phone
        user.country = new_country
        user.city = new_city
        user.city_index = new_city_index
        try:
            user.save()
            return HttpResponse(f"<h2>Данные изменены</h2>"
                                f"<a href = '/'>На главную</a>")
        except Exception as err:
            import datetime
            print(f'[{datetime.datetime.now().strftime("%d/%b/%Y %H:%M:%S")}] Error: {err}')
            return HttpResponse(f"<h2>Что-то пошло не так</h2>")


def delete(request, id):
    try:
        user = Users.objects.get(id=id)
        user.delete()
        return HttpResponse(f"<h2>Пользователь удален</h2>"
                            f"<a href = '/'>На главную</a>")

    except Users.DoesNotExist:
        return HttpResponse("<h2>Такого пользователя нет в таблице</h2>")