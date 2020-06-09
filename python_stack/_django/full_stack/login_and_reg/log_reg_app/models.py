from __future__ import unicode_literals
from datetime import date
import re
from django.db import models


# Create your models here.

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors["first_name"] = "First name should be at least 2 characters."
        if len(postData['lname']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters."     
        if postData['bday'] == '':
            errors['no_bday'] = "Please enter your birthday."
        #bday prints as : 1961-02-02
        # dob = postData['bday']
        # today = date.today()
        # if (dob.year + 13, dob.month, dob.day) > (today.year, today.month, today.day):
        #     errors['under_13'] = "Must be at least 18 years old to register"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Please enter a valid email address.")    
        if len(postData['password']) < 8:
            errors['pw_length'] = "Password should be at least 8 characters."
        if postData['password'] != postData['conf_password']:
            errors['pw_match'] = "Passwords must match."
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    birthday = models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

