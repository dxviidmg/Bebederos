from django import template
from ..models import *

register = template.Library()

@register.assignment_tag
def anio_convocatoria():
    año = Año.objects.first()
    return año