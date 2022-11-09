from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
GAME_PART = ((0, "Long"), (1, "Short"), (2, "Putting"))


class TipsPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('Feautured Image', default='placeholder')
    stance_image = CloudinaryField('Stance Image', default='placeholder')
    stance_content = models.TextField()
    swing_image = CloudinaryField('Swing Image', default='placeholder')
    swing_content = models.TextField()
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    part_of_game = models.IntegerField(choices=GAME_PART, default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def long_or_short(self):
        return self.part_of_game


class Comment(models.Model):
    post = models.ForeignKey(
        TipsPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
