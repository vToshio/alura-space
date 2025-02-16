from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'legenda', 'data_fotografia', 'publicada')
    list_display_links = ('id', 'nome')
    list_filter = ('categoria', )
    list_editable = ('publicada',)
    list_per_page = 10
    search_fields = ('id', 'nome')

# Register your models here.
admin.site.register(Fotografia, ListandoFotografias) # Registra uma tabela do banco de dados na página de admin