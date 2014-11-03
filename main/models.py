from django.db import models


class Message(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    content = models.TextField()

    def __unicode__(self):
        return "%s" % self.name