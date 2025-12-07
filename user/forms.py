from django.forms import ModelForm
from .models import Userlist

class UserForm(ModelForm):
    class Meta:
        model = Userlist
        fields = "__all__"