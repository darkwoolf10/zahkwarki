from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='author')
    for_whom = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='for_whom')
    text = models.TextField()
    punishment_count = models.PositiveIntegerField()
    punishment_type = models.CharField(max_length=50)
    punishment_quantity = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text

    def snippet(self):
        return self.text[:50] + '...'

    def simple_users(self):
        return self.objects.exclude(username='admin')


class CodexPost(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
