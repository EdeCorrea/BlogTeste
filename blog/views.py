from enum import auto
from django.shortcuts import render
from blog.models import Post
from blog.models import Comentario

# Create your views here.

def home(request):
    posts = Post.objects.all()
    dados = {"posts": posts}
    return render(request, 'home.html', dados)

def post(request, pk):
    post = Post.objects.get(pk=pk)
    comentarios_deste_post = Comentario.objects.filter(post=pk)
    dados = {"post": post,
             "comentarios": comentarios_deste_post
            }
    return render(request, 'post.html', dados)


def criar_comentario(request, pk):
    if request.method == "POST":
        post = Post.objects.get(pk=pk)
        comentario = request.POST.get('comentario')
        if request.user.is_authenticated:
            autor = request.user
        else:
            autor = None
             
        Comentario.objects.create(post=post,
                                comentario=comentario,
                                autor=autor)
    return render(request, 'cria-comentario.html')


