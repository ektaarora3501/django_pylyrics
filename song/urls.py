from django.urls import path
from . import views

urlpatterns=[
        path('',views.index,name='home'),
        path('signup',views.Signup,name='signup'),
        path('confirm/<name>',views.Confirm,name='confirm'),
        path('songform',views.Song,name='song-form'),
        path('lyrics/<singer>/<song>',views.Lyrics,name='lyrics'),

        #path('accounts/login',view.)

]
