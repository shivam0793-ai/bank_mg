from django.db import models
from django.core import validators
from django.contrib.auth.models import User
# Create your models here.




class create_account_model(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone_number = models.CharField(
        max_length=10,
        unique=True,
        validators=[validators.MinLengthValidator(10),validators.MaxLengthValidator(10)]
    )

    pincode = models.CharField(max_length=6, validators=[validators.MinLengthValidator(6),validators.MaxLengthValidator(6)])

    aadhaar_number = models.CharField(
        max_length=12,
        unique=True,
        validators=[validators.MinLengthValidator(12),validators.MaxLengthValidator(12)]
    )

    account_number = models.CharField(
        max_length=12,
        unique=True,
        blank=True
    )

    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)


class Transaction_History_moduel(models.Model):
    sender_acc=models.CharField(max_length=12,unique=True)
    reciver_acc=models.CharField(max_length=12,unique=True)
    ammount=models.DecimalField(max_digits=12,decimal_places=2,default=0.0)


