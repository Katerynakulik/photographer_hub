from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Photoshoot

@login_required
def delete_session(request, pk):
    # Перевірка, чи це фотограф
    if not request.user.userprofile.is_photographer:
        messages.error(request, "Only photographers can perform this action.")
        return redirect('home')

    if request.method == 'POST':
        session = get_object_or_404(Photoshoot, pk=pk)
        session.delete()
        messages.success(request, "Photoshoot deleted successfully.")
    
    return redirect('dashboard')