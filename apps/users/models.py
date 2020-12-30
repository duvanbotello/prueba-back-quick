from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class UsersManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, token, age, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            token=token,
            age=age,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, token, age, password=None):
        user = self.create_user(
            email=email,
            first_name=first_name,
            password=password,
            last_name=last_name,
            token=token,
            age=age,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    first_name = models.CharField('First Name', max_length=128, blank=False)
    last_name = models.CharField('Last Name', max_length=128, blank=False)
    email = models.EmailField('Email', max_length=255, unique=True, blank=False)
    token = models.CharField('Token', max_length=128, blank=False)
    age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    image = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=128, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UsersManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'token', 'age', 'password']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

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

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
