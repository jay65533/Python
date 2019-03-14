from __future__ import unicode_literals
from django.db import models

# Create your models here.
# Require the course name to be more than 5 characters 
# description to be more than 15 characters.
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Blog name should be at least 5 characters"
        if len(postData['description']) < 15:
            errors["desc"] = "Blog description should be at least 10 characters"
        return errors
class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    def __repr__(self):
            return "<User object: {}>".format(self.name)
    objects = BlogManager()
class Description(models.Model):
    desc = models.TextField()
    moss = models.OneToOneField(Course, primary_key=True, related_name = "course_id")
