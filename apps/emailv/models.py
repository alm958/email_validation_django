from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]*$')

class EmailManager(models.Manager):
    def add_email(self, **kwargs):
        message_list = []
        state = False
        if Email.objects.filter(email=kwargs['email']).exists():
            message_list.append('email entered already exists.')
        elif not EMAIL_REGEX.match(kwargs['email']):
            message_list.append('Invalid e-mail address entered. Please enter valid email address.')
        if len(message_list) is 0 :
            Email.objects.create(email=kwargs['email'])
            message_list.append('Email {} successfully added'.format(kwargs['email']))
            state = True
        else :
            state = False
        return (state, message_list)

    def getemails(self):
        return Email.objects.all()

    def del_prompt(request, id):
        email = Email.objects.get(id=id)
        context = {
        'email' : email
        }
        return render(request, 'emailv/delete_prompt.html', context )

# Create your models here.
class Email(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = EmailManager()
