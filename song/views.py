from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from song.models import Regis
from django.contrib.auth.decorators import login_required
from song.forms import SignupForm,SongForm
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
# Create your views here.
from  PyLyrics import *

def index(request):
    return render(request,'index.html')


def Signup(request):
    if request.method=='POST':
       form =SignupForm(request.POST)
       print("post")

       if form.is_valid():
           user=form.cleaned_data['user_name']
           print(user)
           us=Regis()
           #url=confirm/user
           print("form valid")
           us.first_name=form.cleaned_data['first_name']
           us.last_name=form.cleaned_data['last_name']
           us.password=form.cleaned_data['password']
           us.user_name=form.cleaned_data['user_name']
           us.email=form.cleaned_data['email']

           us.save()


           return HttpResponseRedirect(reverse('confirm',args=(user,)))

    else:
        #proposed_date=datetime.date.today()+datetime.timedelta(weeks=3)

        form=SignupForm()

    context={
    'form':form,
    #'book_instance':book_instance,
    }

    return render(request,'user_form.html',context)



def Song(request):
    if request.method=='POST':
       form =SongForm(request.POST)
       print("post")

       if form.is_valid():
           singer=form.cleaned_data['singer_name']
           song=form.cleaned_data['song_name']
           ly=PyLyrics.getLyrics((singer),(song))
           print(ly)

           print('here')
           print(singer,song)

           return HttpResponseRedirect(reverse('lyrics',args=(singer,song)))

    else:
        #proposed_date=datetime.date.today()+datetime.timedelta(weeks=3)

        form=SongForm()

    context={
    'form':form,
    #'book_instance':book_instance,
    }

    return render(request,'song_ly.html',context)


def Lyrics(request,singer,song):
           print(singer,song)
           try:
               ly=PyLyrics.getLyrics((singer),(song))
               print(ly)

           except:
               raise ValidationError(_('the singer or song not found'))

           context={
           'singer':singer,
           'song':song,
           'ly':PyLyrics.getLyrics((singer),(song)),
           }

           return render(request,'lyrics.html',context)

def Confirm(request,name):
    user=get_object_or_404(Regis,user_name=name)

    context={
    'name':name,
    }
    return render(request,'confirm.html',context=context)
