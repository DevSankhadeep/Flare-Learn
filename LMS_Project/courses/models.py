from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="profiles/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True, default="")

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    description = models.TextField(blank=True, null=True)
    lessons_count = models.PositiveIntegerField(default=0)
    duration = models.CharField(max_length=50, blank=True, null=True)  # e.g., "10h 30m"
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to="courses/", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
