from django.db import models

# Create your models here.
from django.utils import timezone

from users.models import SiteUser


class Post(models.Model):
    content = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.content[:5]

    # @property
    # def number_of_comments(self):
    #     return Comment.objects.filter(post_connected=self).count()
