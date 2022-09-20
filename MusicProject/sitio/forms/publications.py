
from django import forms

from tuneup.models.publications import MusicHit


class HitPublicationForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        audio_field = self.fields['audio']
        audio_field.widget.attrs.setdefault('accept', 'audio/*')
    
    class Meta:
        model = MusicHit
        fields = ('title', 'cover', 'audio')