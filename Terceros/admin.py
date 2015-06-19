from django.contrib import admin
from .models import Tipo_identificacion, Ciudad, Proveedor, Cliente

admin.site.register(Tipo_identificacion)
admin.site.register(Ciudad)
admin.site.register(Proveedor)
admin.site.register(Cliente)