from django import forms
from pedidos.models import Pedido

class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido

        fields = [
            'responsable',
            'destino',
            'cantidad',
            'album_p',
            'fecha',
            'contacto',
            'estado',
            'observaciones',

        ]

        labels ={
            'reponsable': 'Responsable',
            'destino': 'Destino',
            'cantidad':'Cantidad',
            'album_p':'Album',
            'fec':'Fecha',
            'contacto':'Contacto',
            'estado':'Estado',
            'observaciones':'Observaciones',
        }
        widgets = {
            'responsable': forms.TextInput(attrs={'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'album_p': forms.TextInput(attrs={'class': 'form-control'}),
            
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
            
        }