from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return self.category_name


class Announcement(models.Model):
    announcement_date_time = models.DateTimeField(auto_now_add=True)
    announcement_title = models.CharField(max_length=255)
    announcement_text = RichTextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    category = models.ManyToManyField('Category', through='AnnouncementCategory')

    def preview(self):
        return self.announcement_text[:125] + '...'

    def __str__(self):
        return f'{self.announcement_title.title()}: {self.announcement_text[:20]}... (Автор: {self.author})'

    def get_absolute_url(self):
        return reverse('announcement', args=[str(self.id)])


class AnnouncementCategory(models.Model):
    announcement = models.ForeignKey('Announcement', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Comment(models.Model):
    comment_text = models.TextField()
    comment_date_time = models.DateTimeField(auto_now_add=True)
    announcement = models.ForeignKey('Announcement', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

