from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from tuneup.repository import is_verified_email

def HomeView(request):
    context = {}
    return render(request, 'home.html', context)

@login_required
def UserProfile(request):
    
    context = {
        'email_verified': request.user.is_verified,
    }
    
    return render(request, 'account/profile.html', context)

def view_404(request,exception=None):
    return redirect('home')
