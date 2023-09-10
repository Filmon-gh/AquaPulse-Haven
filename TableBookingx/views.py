from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm
from .models import Reservation 
# Create your views here.

def home_view(request):
    return render(request, 'home.html')
   

@login_required
def reservation_form(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()

    # Query reservations for the current user
    reservations = Reservation.objects.filter(user=request.user)

    return render(request, 'reservation_form.html', {'form': form, 'reservations': reservations})
    
def reservation_success(request):
    return render(request, 'reservation_success.html')
