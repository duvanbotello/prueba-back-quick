from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Users(models.Model):
    first_name = models.CharField('First Name', max_length=128, blank=False)
    last_name = models.CharField('Last Name', max_length=128, blank=False)
    email = models.EmailField('Email', max_length=255, unique=True, blank=False)
    password = models.CharField('Password', max_length=128, blank=False)
    token = models.CharField('Token', max_length=128, blank=False)
    age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    image = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=128, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'token']

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'

    @staticmethod
    def edit_user_patch(request):
        field_update = {}
        try:
            if request.data['first_name']:
                field_update['first_name'] = request.data['first_name']
        except:
            pass
        try:
            if request.data['last_name']:
                field_update['last_name'] = request.data['last_name']
        except:
            pass
        try:
            if request.data['email']:
                field_update['email'] = request.data['email']
        except:
            pass
        try:
            if request.data['password']:
                field_update['password'] = make_password(request.data['password'])
        except:
            pass
        try:
            if request.data['token']:
                field_update['token'] = request.data['token']
        except:
            pass
        try:
            if request.data['age']:
                field_update['age'] = request.data['age']
        except:
            pass
        try:
            if request.data['image']:
                field_update['image'] = request.data['image']
        except:
            pass
        try:
            if request.data['description']:
                field_update['description'] = request.data['description']
        except:
            pass
        return field_update

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)
