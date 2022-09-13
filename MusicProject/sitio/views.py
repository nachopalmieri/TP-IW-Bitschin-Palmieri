from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def HomeView(request):
    context = {}
    return render(request, 'home.html', context)

@login_required
def UserProfile(request):
    return render(request, 'account/profile.html')

def view_404(request, exception=None):
    return redirect('home')
