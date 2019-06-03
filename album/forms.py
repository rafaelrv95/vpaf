from django import forms
from album.models import Album

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album

        fields = [
            'fundacion',
            'cantidad',

        ]

        labels ={
            'fundacion': 'Fundacion',
            'cantidad': 'Cantidad',
        }
        widgets = {
            'fundacion': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            
        }