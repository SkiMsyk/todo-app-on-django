import imp
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
import uuid

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Please input your email address.")
        
        user = self.model(
            email=self.normalize_email(email)
        )
        
        if not password:
            raise ValueError("Please input password.")
        
        user.set_password(password)
        user.admin=False
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    
    class Meta:
        db_table = 'users'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mail = models.EmailField(
        verbose_name='e-mail',
        max_length=255,
        unique=True
    )
    name = models.CharField(blank=False, max_length=255, unique=True)
    admin = models.BooleanField(default=False)
    
    objects = UserManager()
    USERNAME_FIELD = 'name'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.name
    
    
    def has_perm(self, perm, obj=None):
        return self.admin


    def has_module_perms(self, app_label):
        return self.admin
    
    
    @property
    def is_admin(self):
        return self.admin
    
    
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
        
        
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)