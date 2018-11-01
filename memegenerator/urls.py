from django.urls import path
from . import views

app_name='memegenerator'
urlpatterns=[
    path('',views.get_meme,name='home'),
    
]