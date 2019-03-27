from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
# Inside models.py
class BlogManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        
        if ((len(postData['reg_first_name']) < 2) or postData['reg_first_name'].isalpha() == False):
            errors["reg_first_name"] = "First name must include at least 2 characters and only alphabets."
            
        if ((len(postData['reg_last_name']) < 2) or postData['reg_last_name'].isalpha() == False):
            errors["reg_last_name"] = "Last name must include at least 2 characters and only alphabets."
            
        if not EMAIL_REGEX.match(postData['reg_email']):
            errors["reg_email"] = "This email is not valid."
            
        if User.objects.filter(email = postData['reg_email']):
            errors["reg_email"] = "This email already exists."
            
        if (len(postData['reg_password'])) < 8:
            errors["reg_password"] = "Password must include no fewer than eight characters."
            
        if (postData['reg_confirm'] != postData['reg_password']):
            errors["reg_confirm"] = "Password does not match."
        
        return errors

    def login_validator(self, postData):
        errors = {}
        if not User.objects.filter(email = postData['log_email']):
            errors["log_email"] = "This email does not exist"

        if User.objects.filter(email = postData['log_email']):
            hashed = User.objects.get(email = postData['log_email']).password.encode('utf-8')
            #hashed = hashed.encode('utf-8')
            password = postData['log_password'].encode('utf-8')
            #password = password.encode('utf-8')
            if not bcrypt.hashpw(password, hashed) == hashed:
                errors["log_password"] = "This password is invalid."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BlogManager()
    def __repr__(self):
        return "<User object: {} {} {}>".format(self.first_name, self.last_name, self.email)

class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, related_name = "user_message")
    def __repr__(self):
        return "<User object: {} {}>".format(self.message, self.user)

class Comments(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, related_name = "user_comment")
    message = models.ForeignKey(Message, related_name = "comment_message")
    def __repr__(self):
        return "<User object: {} {} {}>".format(self.comment, self.user, self.message)

