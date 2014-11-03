# -*- coding: utf-8 -*-
# from django.db import models
from google.appengine.ext import db


# https://cloud.google.com/appengine/docs/python/datastore/datamodeling
# DB datastore model 적용


class Greeting(db.Model):
    name = db.StringProperty(required=True)  # CharField => StringProperty
    message = db.StringProperty(required=True)

    def __unicode__(self):
        return "%s  by %s" % (self.message, self.name)
