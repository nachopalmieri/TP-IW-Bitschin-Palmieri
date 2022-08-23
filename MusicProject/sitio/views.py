from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from toneup.repository import is_verified_email

def HomeView(request):
    context = {}
    return render(request, 'home.html', context)

@login_required
def UserProfile(request):
    
    context = {
        'email_verified': is_verified_email(request.user.email),
    }
    
    return render(request, 'account/profile.html', context)

def view_404(request,exception=None):
    return redirect('home')
