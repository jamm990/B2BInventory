from django.db import models

class Tipo_identificacion(models.Model):
    td_descripcion = models.CharField(max_length=255)

    def __unicode__(self):
    	return unicode(self.td_descripcion)

class Ciudad(models.Model):
    ciud_nombre_ciudad = models.CharField(max_length=255)
     
    def __unicode__(self):
        return self.ciud_nombre_ciudad

class Proveedor(models.Model):
    prov_NIT = models.CharField(max_length=50)
    prov_razon_social = models.CharField(max_length=100)
    prov_nombres_contacto = models.CharField(max_length=100)
    prov_apellidos_contacto = models.CharField(max_length=100)
    prov_direccion = models.CharField(max_length=100)
    prov_telefono_fijo = models.CharField(max_length=50)
    prov_telefono_movil = models.CharField(max_length=50, blank=True)
    prov_email = models.EmailField()
    prov_comentarios = models.TextField(blank=True)

    def __unicode__(self):
        return self.prov_razon_social

class Cliente(models.Model):
    td_id_tipo_documento = models.ForeignKey(Tipo_identificacion)
    cli_Ndocumento = models.CharField(max_length=50)
    cli_razon_social = models.CharField(max_length=100)
    cli_nombre_contacto = models.CharField(max_length=100)
    ciud_id_ciudad = models.ForeignKey(Ciudad)
    cli_direccion = models.CharField(max_length=100)
    cli_telefono_fijo = models.CharField(max_length=50)
    cli_telefono_movil = models.CharField(max_length=50, blank=True)
    cli_email = models.EmailField()
    cli_comentarios = models.TextField(blank=True)      

    def __unicode__(self):
        return self.cli_razon_social

