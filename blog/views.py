from django.shortcuts import render
from blog.models import Post
from blog.models import Comentario

# Create your views here.

def home(request):
    """
    -> Exibe a paǵina home.
    posts: Lista de todos os posts
    post_mais_recente: Filtra o post mais recente
      
    """
    posts = Post.objects.all()
    post_mais_recente = Post.objects.latest('id')
    dados = {"posts": posts,
             "post_mais_recente": post_mais_recente}
    return render(request, 'home.html', dados)

def post(request, pk):
    """
    -> Exibe os detalhes de um post específico.
    post: Seleciona um post específico
    post_mais_recente: Filtra o post mais recente
    comentarios_deste_post: Lista os comentários específicos para o post selecionado
      
    """
    
    post = Post.objects.get(pk=pk)
    post_mais_recente = Post.objects.latest('id')
    comentarios_deste_post = Comentario.objects.filter(post=pk).order_by('id')
    dados = {"post": post,
             "comentarios": comentarios_deste_post,
             "post_mais_recente": post_mais_recente
            }
    return render(request, 'post.html', dados)


def criar_comentario(request, pk):
    """
    -> Cria comentário para um post específico.
    post: Seleciona (pelo atributo pk) o post que será comentado 
    comentario: Comentário enviado pelo usuário
    autor: Autor do post. Pode ser ou não um usuário cadastrado no sistema.
      
    """
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


