from django.contrib import admin
from .models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ("criado_por",)

    def save_model(self, request, obj, form, change):
        usuario = request.user
        obj.criado_por = usuario
        super(CategoriaAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(CategoriaAdmin, self).get_queryset(request)
        qs = qs.filter(criado_por=request.user)
        return qs


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "descricao", "categoria", "endereco_entrega")
    list_filter = ("categoria",)
    list_editable = ("preco",)
    list_display_links = ("nome", "descricao", "endereco_entrega")
    search_fields = ("nome", "descricao", "endereco_entrega")
