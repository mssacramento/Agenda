from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nte', 'nome', 'gestor', 'telefoneprinc', 'emailprinc', 'mostrar',)
    list_display_links = ('nome',)
    list_per_page = 20
    search_fields = ('nte', 'nome',)
    list_editable = ('telefoneprinc', 'mostrar')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
