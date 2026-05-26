from django.db import models
from django.core.validators import MinLengthValidator

# 1. IMAGEN 2: Model per a les Etiquetes (Tag)
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

# 2. IMAGEN 3: Model per als Autors (Author)
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def total_posts(self):
        return self.posts.count()

# 3. IMAGEN 1: Model per als Posts del Blog
class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    
    # Relacions entre taules
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title