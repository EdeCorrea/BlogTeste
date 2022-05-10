from django.contrib import admin

# Register your models here.
from blog.models import Post
from blog.models import Comentario

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_diplay = ('id', 'titulo', 'conteudo', )
    readonly_fields = ( 'autor', 'data_criacao',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.autor = request.user
            obj.save()
        super(PostAdmin, self).save_model(request, obj, form, change)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    
    readonly_fields = ('id', 'post', 'comentario', 'autor', 'data_criacao')

    

