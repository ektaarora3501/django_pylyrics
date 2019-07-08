from django.forms import PasswordInput,forms,CharField,EmailField
from song.models import Regis
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class SignupForm(forms.Form):
    first_name=CharField(max_length=100)
    last_name=CharField(max_length=100)
    user_name=CharField(max_length=100)
    email=EmailField()
    password=CharField(max_length=12,widget=PasswordInput)
    cnf_pass=CharField(max_length=12,widget=PasswordInput)

    def clean_cnf_pass(self):
        print('here')
        pas=self.cleaned_data['password']
        cnf=self.cleaned_data['cnf_pass']
        if cnf !=pas:
            raise ValidationError(_("please reconfirm your password"))
        print(cnf)

        return cnf

    def clean_user_name(self):
        name=self.cleaned_data['user_name']
        if Regis.objects.filter(user_name=name).exists():
            raise ValidationError(_(" The given username already exists"))

        return name

    def clean_email(self):
        name=self.cleaned_data['email']
        if Regis.objects.filter(email=name).exists():
            raise ValidationError(_(" The given Email already exists"))

        return name


class SongForm(forms.Form):
    singer_name=CharField(max_length=100)
    song_name=CharField(max_length=100)
