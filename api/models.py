from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# This class implements a model that creates new "employees" of the credit union. It uses most of Django's base fields, but there's a
# few that are introduced to fit credit union needs including limiting how much money tellers are allowed to release to member
# before a manager override is required and how mnay fees an employee can refund.
# Documentation can be found here: https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#substituting-a-custom-user-model
class User(AbstractUser):
    # inlcude which fields are needed for the user model if using AbstractUser.
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    staff_level = models.IntegerField()
    # Considering adding a staff title in the future.
    # staff_title
    # check_hold_limit = models.integerField()
    # fee_refund_limit = models.integerField()
    # Once you start extending the base user model in Django, you'll need to 
    # include which fields are required.
    REQUIRED_FIELDS = ['email', 'staff_level']
    pass

class Member(models.Model):
    # Documentation on choice field options can be found here: https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.Field.choices
    PREFIX_CHOICES = [
        ('Mr', 'Mister'),
        ('Mrs', 'Mistress'),
        ('Ms', 'Missus'),
    ]
    SUFFIX_CHOICES = [
        ('Jr', 'Junior'),
        ('Sr', 'Senior'),
        ('II', 'Second'),
        ('III', 'Third'),
        ('IV', 'Fourth'),
    ]
    PRONOUN_CHOICES = [
        ('He', 'He/Him/His'),
        ('She', 'She/Her/Hers'),
        ('They', 'They/Them/Theirs'),
    ]
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    middle_name = models.CharField(max_length = 100, null = True)
    prefix = models.CharField(max_length= 10, null = True, choices=PREFIX_CHOICES)
    suffix = models.CharField(max_length = 10, null = True, choices=SUFFIX_CHOICES)
    pronouns = models.CharField(max_length = 25, null = True, choices=PRONOUN_CHOICES)
    verbal_password = models.CharField(max_length=100)
    ssn = models.IntegerField(validators=[MinValueValidator(100000000), MaxValueValidator(999999999)])
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null = True)
    join_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=10)
    email = models.EmailField(null = True)
    # Altered field type from integer to string since I was having issues with min/max values.
    home_number = models.CharField(max_length=10, null=True)
    mobile_number = models.CharField(max_length=10, null=True)
    work_number = models.CharField(max_length=10, null=True)