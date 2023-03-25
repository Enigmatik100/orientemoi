import uuid

from django.db import models
from phone_field import PhoneField

from orientation.utils.helpers import gen_question_code


class Question(models.Model):
    code = models.CharField(unique=True, default=gen_question_code)
    content = models.TextField(max_length=250, blank=True, null=True, default='')
    category = models.ForeignKey('Category', related_name='category', on_delete=models.CASCADE)
    profil = models.ForeignKey('Profil', related_name='profil', on_delete=models.CASCADE)

    class Meta:
        db_table = "questions"


class ClosedQuestion(Question):
    is_checked = models.BooleanField(default=False)

    class Meta:
        db_table = "open_questions"


class OpenQuestion(Question):
    CHOICES = (
        (1, 'Faible'),
        (1, 'Moyen'),
        (1, 'Fort')
    )
    choices = models.CharField(default=False, choices=CHOICES)

    class Meta:
        db_table = "closed_questions"


class Category(models.Model):
    """
    Intérêts et activités / 2- Intérêts et occupations/ 3- Aptitudes / 4- Personnalités
    """
    code = models.CharField(max_length=50, blank=False, null=False, unique=True)
    label = models.TextField(max_length=250, blank=True, null=True, default='')
    description = models.TextField(max_length=250, blank=True, null=True, default='')

    class Meta:
        db_table = "categories"


class Profil(models.Model):
    """
    Realiste, Investigateur, Artiste,Social, Entrepreneur, Conventionnel
    """
    code = models.CharField(max_length=1, blank=False, null=False, unique=True)
    label = models.CharField(max_length=100, blank=False, null=False, default='')
    description = models.TextField(max_length=100, blank=True, null=True, default='')

    class Meta:
        db_table = "profils"

class Test(models.Model):
    """Association table between User and question"""
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    question = models.ForeignKey('Team', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'team_user'
        ordering = ['created_at']

class UserResponse(models.Model):
    """Association table between User and question"""
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    question = models.ForeignKey('Team', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'team_user'
        ordering = ['created_at']


class User(models.Model):
    """
     Class for user
     """
    TYPES_SEX = [
        ('M', 'M'),
        ('F', 'F'),
    ]

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    last_name = models.CharField(max_length=100, blank=True, null=True, default='')
    first_name = models.CharField(max_length=100, blank=True, null=True, default='')
    email = models.EmailField(blank=False, null=False, default='', unique=True)
    mobile_phone = PhoneField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"
