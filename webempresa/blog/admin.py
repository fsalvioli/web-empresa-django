from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','author','published','post_categories')
    ordering = ('author',) # es una tupla
    search_fields = ('title','content','author__username', 'categories__name')# campos de busqueda, para buscar una primaryKey es un poco diferente cono en author
    date_hierarchy = 'published'
    list_filter = ('author__username',)

    def post_categories(self, obj):
        return ", ".join([cat.name for cat in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)