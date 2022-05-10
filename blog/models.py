from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    """
    -> Tabela de Posts
    :atributo titulo: Título do post
    :atributo conteudo: Conteúdo do post
    :atributo autor: Autor do post.
    :atributo data_criacao: Data da criação do post
    
    ordenação: pelo post mais recente
    """
    titulo = models.CharField(max_length=200)
    conteudo = RichTextUploadingField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-data_criacao',)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    """
    -> Tabela de Comentários
    :atributo post: post referente ao comentário
    :atributo comentario: Comentário sobre o post.
    :atributo autor: Autor do post. Pode ser ou não um usuário cadastrado no sistema.
    :atributo data_criacao: Data da criação do comentário
    
    ordenação: pelo post mais antigo
    """
    post = models.ForeignKey('Post', on_delete=models.PROTECT, blank=True,null=True)
    comentario = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

