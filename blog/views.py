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
    dados = {"post": post}
    return render(request, 'post.html', dados)


def criar_comentario(request, pk):
    if request.method == "GET":
        return render(request, 'cria-comentario.html')

    elif request.method == "POST":
        post = Post.objects.get(pk=pk)
        comentario = request.POST.get('comentario')      
        Comentario.objects.create(post=post,
                                comentario=comentario)
        return render(request, 'cria-comentario.html')


