from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from checkout.models import PurchasedPhoto
from bookings.models import Booking

@login_required
def profile(request):
    purchased_photos = PurchasedPhoto.objects.filter(user=request.user).order_by('-purchased_at')
    my_bookings = Booking.objects.filter(user=request.user).order_by('-booked_at')
    
    context = {
        'purchased_photos': purchased_photos,
        'my_bookings': my_bookings,
    }
    return render(request, 'profiles/profile.html', context)