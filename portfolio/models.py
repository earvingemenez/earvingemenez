from django.db import models


class Timeline(models.Model):

    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    year = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    position = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="timeline/", null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.name


class Project(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True, default="#")
    image = models.ImageField(upload_to='projects/', null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.name


class Skill(models.Model):

    name = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.name


class Education(models.Model):

    school = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    course = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.school


class Interest(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.name


class Feedback(models.Model):

    content = models.TextField(null=True)
    author = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.author