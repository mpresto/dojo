from django.db import models
from datetime import datetime, date


# Create your models here.

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title must be greater than 2 characters."

        if postData['form_type'] != 'create':
            update_show = Show.objects.get(id=postData['id'])
            if Show.objects.filter(title__iexact=postData['title']).exists() and postData['title'] != update_show.title:
                    errors['title'] = "This title already exists."
        if postData['form_type'] == 'create':
            if Show.objects.filter(title__iexact=postData['title']).exists():
                errors['title'] = "This title already exists."

        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters."
        if len(postData['desc']) != 0 and len(postData['desc']) < 10:
            errors['desc'] = "Description should be at least 10 characters."

        if postData['release_date'] == '':
            errors['no_date'] = "Please enter a valid date."
        if postData['release_date'] > date.today().strftime('%Y-%m-%d'):
            errors['future_date'] = "Release date must be in the past."
        print(postData['release_date'])

        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
