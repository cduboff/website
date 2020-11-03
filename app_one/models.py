from django.db import models
from datetime import datetime
import re, bcrypt

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9,+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def validator(self, form):
        errors = {}
        if len(form['first_name']) < 2:
            errors['first_name'] = "Name must be at least 2 characters!"
        if len(form['last_name']) < 2:
            errors['last_name'] = "Name must be at least 2 characters!"
        if len(form['username']) < 5:
            errors['username'] = "Username must be at least 5 characters:"
        email_check = self.filter(email_address=form['email_address'])
        if email_check:
            errors['email_address'] = "Email already in use"
        if len(form['password']) < 8:
            errors['password'] = "Password must be at least 8 characters!"
        if form['confirm_password'] != form['password']:
            errors['confirm_password'] = "Password and Confirmation Password do not match"
        return errors

    def authenticate(self, username, password):
        users = self.filter(username=username)
        if not users:
            return False

        user = users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=45)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=25)
    confirm_password = models.CharField(max_length=25)
    likes = models.ManyToManyField(User, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Weeks(models.Model):
    week_num = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Days(models.Model):
    day_of_week = models.CharField(max_length=255)
    week =  models.ForeignKey(Weeks, related_name="days", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Meal(models.Model):
    main_dish = models.TextField()
    side_one = models.TextField()
    side_two = models.TextField()
    side_three = models.TextField()
    drink = models.CharField(max_length=255)
    days = models.ManyToManyField(Days, related_name="meal")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)