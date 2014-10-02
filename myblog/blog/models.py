from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField('Time Published')
    content = models.TextField(max_length=10000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id
