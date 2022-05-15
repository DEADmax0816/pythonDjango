from .models import Users
import django.forms as forms


class UsersForm(forms.Form):
    text_fio = forms.CharField(max_length=500)
    text_phone = forms.CharField(max_length=50)
    text_country = forms.CharField(max_length=200)
    text_city = forms.CharField(max_length=200)
    text_city_index = forms.CharField(max_length=100)
    text_place = forms.CharField(max_length=200)

    '''
    class Meta:
        model = Users
        fields = ["fio", "phone", "country", "city", "city_index"]
        widgets = {
            "fio": TextInput(attrs={'type': 'text'}),
            "phone": TextInput(attrs={'type': 'text'}),
            "country": TextInput(attrs={'type': 'text'}),
            "city": TextInput(attrs={'type': 'text'}),
            "city_index": TextInput(attrs={'type': 'text'})
        }
    '''