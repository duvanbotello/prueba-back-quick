from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Users(models.Model):
    first_name = models.CharField('First Name', max_length=128, blank=False)
    last_name = models.CharField('Last Name', max_length=128, blank=False)
    email = models.EmailField('Email', max_length=255, unique=True, blank=False)
    password = models.CharField('Password', max_length=64, blank=False)
    token = models.CharField('Token', max_length=128, blank=False)
    age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    image = models.ImageField(upload_to='profile/', max_length=255, null=True, blank=True)
    description = models.CharField(max_length=128, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'token']

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'
