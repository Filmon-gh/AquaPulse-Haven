from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('reservation/', views.reservation_form, name='reservation'),
    path('reservation/success/',
         views.reservation_success, name='reservation_success'),
    path('reservation/update/<int:reservation_id>/',
         views.update_reservation, name='update_reservation'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservation/delete/<int:reservation_id>/',
         views.delete_reservation, name='delete_reservation'),
]


