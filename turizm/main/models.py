from django.db import models


class Users(models.Model):
    fio = models.TextField()
    phone = models.TextField(unique=True)
    country = models.TextField()
    city = models.TextField()
    city_index = models.TextField()

    def __str__(self):
        return f'User {self.fio}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Countries(models.Model):
    country = models.TextField()

    def __str__(self):
        return f'Country {self.country}'

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Tickets(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

    def __str__(self):
        return f'Ticket {self.id}'
