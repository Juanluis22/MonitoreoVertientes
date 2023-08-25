from django.shortcuts import render
from django.views.generic import TemplateView
from nucleo.models import habitantes

class Selector(TemplateView):
    template_name = 'selector/selector.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener el habitante actual
        habitante = habitantes.objects.get(usuario=self.request.user)

        # Obtener la comunidad y las vertientes asociadas al habitante
        comunidad_habitante = habitante.comunidad
        context['comunidad_habitante'] = comunidad_habitante
        if comunidad_habitante:
            # Obtén las vertientes asociadas a la comunidad del habitante
            vertientes_comunidad = comunidad_habitante.vertiente_set.all()
            context['vertientes_comunidad'] = vertientes_comunidad
        
        return context
