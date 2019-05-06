from django.db import models



class Article(models.Model):
    created =  models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    summary = models.TextField()
    link = models.URLField()

    class Meta:
        ordering = ('created',)
