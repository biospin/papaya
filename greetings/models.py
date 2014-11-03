from django.db import models


class Greeting(models.Model):
    name = models.CharField(max_length=30)
    message = models.CharField(max_length=150)

    def __unicode__(self):
        return "%s  by %s" % (self.message, self.name)
