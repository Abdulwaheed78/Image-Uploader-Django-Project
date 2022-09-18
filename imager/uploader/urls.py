from django.urls import path
from uploader import views

urlpatterns=[
    path('',views.index,name='index',)
]

