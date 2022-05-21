from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    form = UsersForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            fio = form.cleaned_data.get('text_fio')
            phone = form.cleaned_data.get('text_phone')
            country = form.cleaned_data.get('text_country')
            city = form.cleaned_data.get('text_city')
            city_index = form.cleaned_data.get('text_city_index')
            place = form.cleaned_data.get('text_place')

            if not Countries.objects.filter(country=place).exists():
                return redirect('country-error')

            newUser = Users(fio=fio, phone=phone, country=country, city=city, city_index=city_index)

            try:
                newUser.save()
            except Exception:
                return HttpResponse('<h1>Пользователь с таким номером уже существует</h1>')

            u = Users.objects.filter(phone=phone)
            c = Countries.objects.filter(country=place)
            u_id = u[0]
            c_id = c[0]
            newTicket = Tickets(user=u_id, country=c_id)
            newTicket.save()

            return HttpResponse("<h1>Данные отправлены успешно</h1>"
                                "<a href = '/'>Назад</a>")

        else:
            return HttpResponse('<h1>Форма невалидна</h1>')
    context = {
        'form': form
    }
    return render(request, 'main/index.html', context)


def country_error(request):
    return HttpResponse("<h1>Страны, в которую вы хотите отправиться, нет в списке</h1>"
                        "<a href = '/'>Назад</a>")


def countries(request):
    counties_list = Countries.objects.all()
    s = ''
    for el in counties_list:
        s += str(el.country) + ' '
    return HttpResponse(f"<h1>{s}</h1>"
                        f"<a href = '/'>Назад</a>")


def tables(request):
    return render(request, 'main/tables.html')


def table_users(request):
    users_list = Users.objects.all()
    s = ''
    for el in users_list:
        s += str(el.id) + ' '
        s += str(el.fio) + ' '
        s += str(el.phone) + ' '
        s += str(el.country) + ' '
        s += str(el.city) + ' '
        s += str(el.city_index) + ' '
        s += '<br>'

    return HttpResponse(f"<h2>{s}</h2>"
                        f"<a href = '/tables'>Назад</a>")


def table_tickets(request):
    tickets_list = Tickets.objects.all()
    s = ''
    for el in tickets_list:
        s += str(el.id) + ' '
        s += str(el.user) + ' '
        s += str(el.country) + ' '
        s += '<br>'
    return HttpResponse(f"<h2>{s}</h2>"
                        f"<a href = '/tables'>Назад</a>")


def select(request):
    users_list = Users.objects.all()
    select_list = []
    for el in users_list:
        temp = []
        s = ''
        s += str(el.id) + ' '
        s += str(el.fio) + ' '
        s += str(el.phone) + ' '
        s += str(el.country) + ' '
        s += str(el.city) + ' '
        s += str(el.city_index) + ' '
        temp.append(el.id)
        temp.append(s)
        select_list.append(temp)

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

    if request.method == 'POST':
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
            except Exception:
                return HttpResponse(f"<h2>Что-то пошло не так</h2>")

    context = {
        'form': form
    }
    return render(request, 'main/update.html', context)


def delete(request, id):
    form = UpdateUserForm(request.POST or None)

    try:
        user = Users.objects.get(id=id)
        user.delete()
        return HttpResponse(f"<h2>Пользователь удален</h2>"
                            f"<a href = '/'>На главную</a>")

    except Users.DoesNotExist:
        return HttpResponse("<h2>Такого пользователя нет в таблице</h2>")