from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _

from sitio.forms.publications import HitPublicationForm

from tuneup.services import publish_new_hit, get_feed_for_user
from tuneup.models.publications import MusicHit, PUB_STATE_ACTIVE

from django.shortcuts import get_object_or_404


def HomeView(request):
    context = { 'publications': get_feed_for_user(request.user) }
    return render(request, 'home.html', context)


@login_required
def UserProfile(request):
    return render(request, 'account/profile.html')


def view_404(request, exception=None):
    return redirect('home')

def publication_detail(request, pk):
    
    queryset = MusicHit.objects.all(state=PUB_STATE_ACTIVE)
    
    return render(request, 'publications/detail_hit.html', context={
        'publication': get_object_or_404(queryset, pk=pk)
    })

@login_required
def create_hit(request):
    
    context = {}
    
    hit_form = HitPublicationForm()
    
    if request.method == 'POST':
        
        hit_form = HitPublicationForm(request.POST, request.FILES)
        
        if hit_form.is_valid():
            
            hit_publication = hit_form.save(commit=False)
            
            try:
                
                hit_publication.author = request.user
                
                publish_new_hit(hit_publication)
            
                messages.success(request, _('New publication created!'))
            
                return redirect('home')
            
            except ValueError as error:
                messages.error(request, error)
    
    context['form'] = hit_form
    
    return render(request, 'publications/create_hit.html', context)