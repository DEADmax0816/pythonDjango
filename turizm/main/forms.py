import django.forms as forms


class UsersForm(forms.Form):
    text_fio = forms.CharField(max_length=500)
    text_phone = forms.CharField(max_length=50)
    text_country = forms.CharField(max_length=200)
    text_city = forms.CharField(max_length=200)
    text_city_index = forms.CharField(max_length=100)
    text_place = forms.CharField(max_length=200)


class UpdateUserForm(forms.Form):
    update_fio = forms.CharField(max_length=500)
    update_phone = forms.CharField(max_length=50)
    update_country = forms.CharField(max_length=200)
    update_city = forms.CharField(max_length=200)
    update_city_index = forms.CharField(max_length=100)