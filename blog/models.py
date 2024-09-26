from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


# Top 12 animes in order of ratings 1-12
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 13)], default=1)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.CharField(max_length=200, default="Custom date string")
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ["rating"]

    def __str__(self):
        return f"{self.title} | Rating: {self.rating}/12"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80, default = "xxx")
    email = models.EmailField(default = "xxx")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"