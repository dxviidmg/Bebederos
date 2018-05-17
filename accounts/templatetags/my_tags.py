from django import template
from ..models import *

register = template.Library()

@register.assignment_tag
def anio_convocatoria():
    anio = Anio.objects.first()
    return anio