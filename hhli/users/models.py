from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class HUserManager(BaseUserManager):
    def create_user(self, **validated_data):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        email               = validated_data.get('email')
        password            = validated_data.get('password')
        confirm_password    = validated_data.get('confirm_password')

        user = self.model(
            email           = self.normalize_email(email),
            first_name      = validated_data.get('first_name',    None),
            last_name       = validated_data.get('last_name',     None),
            gender          = validated_data.get('gender',        None),
            date_of_birth   = validated_data.get('date_of_birth', None),
            height          = validated_data.get('height',        None),
            weight          = validated_data.get('weight',        None)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """

        a = {
                'email': email,
                'password':password,
                'first_name':first_name 
            }

        user = self.create_user(a)
        user.is_admin = True
        user.save(using=self._db)
        return user


class HUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    TITLE_TYPES = (
        ('MRS', 'Mrs'),
        ('MR', 'Mr'),
        ('DR', 'Dr'),
        ('OT', 'Others'),
    )
    title = models.CharField(max_length=5, choices=TITLE_TYPES)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True)
    GENDER_TYPES = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_TYPES)
    date_of_birth = models.DateField(null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_expert = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = HUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name',]

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def is_expert(self):
        # The user is identified by their email address
        return self.is_expert

    def __str__(self):              # __unicode__ on Python 2
        return self.email

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

    @classmethod
    def get_by_id(cls, HUser_id):
        return HUser.objects.get(pk=HUser_id)

class HUserAddress(models.Model):
    HUser = models.ForeignKey('HUser', on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=50, blank=True)
    address_line_2 = models.CharField(max_length=50, blank=True)
    address_line_3 = models.CharField(max_length=50, blank=True)
    address_city = models.CharField(max_length=30, blank=True)
    address_state = models.CharField(max_length=30,blank=True)
    address_country = models.CharField(max_length=30,blank=True)
    address_zip = models.CharField(max_length=10,blank=True)
    contact_no = models.CharField(max_length=15,blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

class Prospect(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=25)
    email_address = models.EmailField(max_length=25)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    # referred_by_id = models.UUIDField(blank=True, default=uuid.uuid4, help_text='HUser UUID',)
    # referred_for_circle_id = models.UUIDField(blank=True, default=uuid.uuid4,
    #                                           help_text='if the referral was to join in a circle, circle UUID',)

    # referred_for_program_id = models.UUIDField(blank=True, default=uuid.uuid4,
    #                                            help_text='if the referral was to subscribe for a program, program UUID',)

class Circle(models.Model):

    name = models.CharField(max_length=50, help_text='name HUser can identify his group with')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    # members_can_refer = models.BooleanField(default=False,
    #                                         help_text='when true, it means '
    #                                                   'members can bring in other members in to this circle')
    # max_number_members = models.SmallIntegerField(help_text='Maximum allowed number of members in the group')
