from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission, Group

class CustomUserManager(BaseUserManager):

    def default_profile_image():
        return 'default_profile_picture.jpg'

    def create_user(self, email, password=None, first_name=None, last_name=None,img=None, role=None ,**extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,img=img, first_name=first_name, last_name=last_name, role=role ,**extra_fields)
        user.setImg('def.png')
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, first_name=None, last_name=None, role='Admin',img=None , **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, first_name, last_name,img, role ,**extra_fields)

class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    img = models.ImageField(upload_to='profile_images/', default='def.png', null=True, blank=True)  # Updated image field
    objects = CustomUserManager()
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_users')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    def __str__(self):
        return self.email

    def set_role(self, new_role):
        self.role = new_role
        self.save()  # Save the instance after updating the role
    def setFN(self,fn):
        self.first_name = fn 
        self.save()

    def setLN(self,fn):
        self.last_name = fn 
        self.save()

    def setImg(self,fn):
        self.img = fn 
        self.save()
      
    def setEmail(self,fn):
        self.email = fn 
        self.save()