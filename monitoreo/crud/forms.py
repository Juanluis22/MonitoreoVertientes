from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from nucleo.models import *

class ComunidadForm(ModelForm):
    class Meta:
        model= comunidad
        fields='__all__'

class VertienteForm(ModelForm):
    class Meta:
        model= vertiente
        fields=['nombre','desc','ubicación','comunidad']
        

class HabitanteForm(ModelForm):
    class Meta:
        model= habitantes
        fields='__all__'
        
        widgets={
            
            'nombre':TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'rut':TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            
            'edad':TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            
            'correo':TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

        }


        
