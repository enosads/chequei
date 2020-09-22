from django.contrib import admin

# Register your models here.
from mobile import models

admin.site.register(models.Usuario)
admin.site.register(models.Endereco)
admin.site.register(models.Vaga)
admin.site.register(models.Evento)
