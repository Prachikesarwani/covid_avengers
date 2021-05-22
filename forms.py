from django.forms import ModelForm, fields
from .models import Register, Registerbtn

class Register(ModelForm):
    class Meta:
        model = Register
        fields = ['name','email','phone','address','date']


class Registerbtn(ModelForm):
    class Meta:
        model = Registerbtn
        fields = ['requirement','Quantity']        