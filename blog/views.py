from django.shortcuts import render
from blog.models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    dados = {"posts": posts}
    return render(request, 'home.html', dados)

def post(request, id):
    post = Post.objects.get(pk=id)
    dados = {"post": post}
    return render(request, 'post.html', dados)
