from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm
from .models import Reservation
from .models import UIElement
from django.contrib import messages
# Create your views here.


def home_view(request):
    ui_element = UIElement.objects.first()
    return render(request, 'home.html', {'ui_element': ui_element})


@login_required  # Apply the login_required decorator
def reservation_list(request):
    reservations = Reservation.objects.all()  # Query your reservations here
    return render(
        request,
        'reservation_list.html',
        {'user': request.user, 'reservations': reservations}
    )


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

    return render(
        request,
        'reservation_form.html',
        {'form': form, 'reservations': reservations}
    )


def reservation_success(request):
    return render(request, 'reservation_success.html')


@login_required
def update_reservation(request, reservation_id):
    reservation = get_object_or_404(
        Reservation, pk=reservation_id, user=request.user
    )

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            # Redirect to a success page or reservation list
            return redirect('reservation_success')
    else:
        form = ReservationForm(instance=reservation)

    return render(
        request,
        'update_reservation.html',
        {'form': form, 'reservation': reservation}
    )


@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(
        Reservation, pk=reservation_id, user=request.user
    )

    if request.method == 'POST':
        # Check if the user confirms the deletion
        if 'confirm_delete' in request.POST:
            reservation.delete()
            messages.success(request, 'Reservation deleted successfully.')
            # Redirect to the reservation list or a success page
            return redirect('reservation_list')
        else:
            # User canceled the deletion, redirect back to the reservation list
            return redirect('reservation_list')

    return render(
        request,
        'delete_reservation.html',
        {'reservation': reservation}
    )
