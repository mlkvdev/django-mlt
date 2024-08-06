from django.db import models
from django_prometheus.models import ExportModelOperationsMixin


class Blog(ExportModelOperationsMixin("Blog"), models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')


class Comment(ExportModelOperationsMixin("Comment"), models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content[:20]
