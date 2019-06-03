from django import forms
from pedidos.models import Pedido

class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido

        fields = [
            'responsable',
            'destino',
            'cantidad',
            'fecha',
            'contacto',
            'observaciones',

        ]

        labels ={
            'reponsable': 'Responsable',
            'destino': 'Destino',
            'cantidad':'Cantidad',
            'fecha':'Fecha',
            'contacto':'Contacto',
            'observaciones':'Observaciones',
        }
        widgets = {
            'responsable': forms.TextInput(attrs={'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
            
        }