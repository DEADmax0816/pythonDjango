from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import UsersForm


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