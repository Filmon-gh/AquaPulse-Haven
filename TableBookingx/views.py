from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm
from .models import Reservation 
# Create your views here.

def home_view(request):
    return render(request, 'home.html')

@login_required  # Apply the login_required decorator
def reservation_list(request):
    reservations = Reservation.objects.all()  # Query your reservations here
    return render(request, 'reservation_list.html', {'reservations': reservations})


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

def update_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            # Redirect to a success page or reservation list
            return redirect('reservation_success')
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'update_reservation.html', {'form': form, 'reservation': reservation}