from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import ugettext_lazy as _

from contact.models import Contact

class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, last_name, first_name, street, npa, city, canton, department, role, password=None, is_married = False, number_of_children = 0):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            last_name=last_name,
            first_name=first_name,
            date_of_birth=date_of_birth,
            department = department,
            street = street,
            npa = npa,
            city = city,
            canton = canton,
            role = role,
            is_married=is_married,
            number_of_children = number_of_children
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password, last_name, first_name, street, npa, city, canton, department, role, is_married = False, number_of_children = 0):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            last_name=last_name,
            first_name=first_name,
            date_of_birth=date_of_birth,
            department = department,
            street = street,
            npa = npa,
            city = city,
            canton = canton,
            role = role,
            is_married=is_married,
            number_of_children = number_of_children
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, Contact):
    DEPARTMENTS = (
        ('A', _('Area manager')),
        ('I', _('IT')),
        ('M', _('Market')),
        ('P', _('Pharmacist manager')),
        ('R', _('Human Resources')),  
    )
    ROLES = (
        ('A', _('Pharmacy assistant')),
        ('D', _('Director')),
        ('E', _('Employee')),
        ('P', _('Pharmacist')),
        ('R', _('Responsable')),       
    )
    last_name = models.CharField(max_length = 64, verbose_name = _("Lastname"))
    first_name = models.CharField(max_length = 64, verbose_name = _("Firstname"))
    email = models.EmailField(max_length = 255, unique=True)
    date_of_birth = models.DateField(verbose_name = _("Date de naissance"))
    is_married = models.BooleanField(blank = True, default=False, verbose_name = _("Est marié(e) ?"))
    number_of_children = models.PositiveSmallIntegerField(default=0,verbose_name = _("Nombre d'enfants"))
    role = models.CharField(max_length = 1, verbose_name = _("Role"), choices = ROLES)
    department = models.CharField(max_length = 1, verbose_name = _("Département"), choices = DEPARTMENTS)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'last_name', 'first_name', 'department', 'role', 'street', 'npa', 'city', 'canton']

    def __str__(self):
        return "{} {} ({})".format(self.last_name, self.first_name, self.get_role_display())

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_name(self):
        return self.first_name

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
