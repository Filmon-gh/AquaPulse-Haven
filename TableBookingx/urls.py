from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('reservation/', views.reservation_form, name='reservation'),
    path('reservation/success/', views.reservation_success, name='reservation_success'),
   
]



