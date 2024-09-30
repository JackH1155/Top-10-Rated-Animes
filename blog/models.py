from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


# Top 12 animes in order of ratings 1-12
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    creator = models.CharField(max_length=100, default="Anonymous")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 13)], default=1)
    decimal_rating = models.DecimalField(
        max_digits=3, decimal_places=1, default=Decimal('1.0'),
        validators=[MinValueValidator(Decimal('1.0')), MaxValueValidator(Decimal('10.0'))]
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.CharField(max_length=200, default="Custom date string")
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ["rating"]

    def __str__(self):
        return f"{self.title} | Rating: {self.rating}/12 | Decimal Rating: {self.decimal_rating}/10.0"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
        related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"