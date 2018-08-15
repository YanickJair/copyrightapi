from django.contrib import admin
from .models import (
    AreaAplicacao,
    Licenca,
    TipoObra,
    TipoPerfil,
    Commentary,
    CommentaryReply,
    Obra
)
# Register your models here.
admin.site.register(AreaAplicacao)
admin.site.register(Licenca)
admin.site.register(TipoObra)
admin.site.register(TipoPerfil)
admin.site.register(Commentary)
admin.site.register(CommentaryReply)
admin.site.register(Obra)