from django.urls import path
from app3 import views


urlpatterns = [
    path('',views.vistas1, name='vista1'),
    path('',views.vistas2, name='vista2'),
]