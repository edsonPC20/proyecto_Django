from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag

# 1. Página de inicio (Muestra los 3 últimos posts)
def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

# 2. Listado de todos los posts
def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/post_list.html", {
        "all_posts": all_posts
    })

# 3. Detalle de un post concreto
def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })

# 4. Listado de Autores
def authors(request):
    all_authors = Author.objects.all()
    return render(request, "blog/authors_list.html", {  # <-- Le añadimos la 's' aquí
        "authors": all_authors  # <-- Cambiado a 'authors' para que tu archivo actual lo entienda
    })
# 5. Detalle de un Autor y sus posts
def author_detail(request, id):
    identified_author = get_object_or_404(Author, pk=id)
    return render(request, "blog/author_detail.html", {
        "author": identified_author
    })

# 6. Listado de Etiquetas (Tags)
def tags(request):
    all_tags = Tag.objects.all()
    return render(request, "blog/tag_list.html", {
        "all_tags": all_tags
    })
# Añade esta función al final de tu archivo blog/views.py
def tag_posts(request, tag_caption):
    # Buscamos la etiqueta exacta por su caption
    tag = get_object_or_404(Tag, caption=tag_caption)
    # Filtramos todos los posts que tengan esa etiqueta asignada
    posts_with_tag = Post.objects.filter(tags=tag).order_by("-date")
    
    return render(request, "blog/tag_posts.html", {
        "tag": tag,
        "posts": posts_with_tag
    })