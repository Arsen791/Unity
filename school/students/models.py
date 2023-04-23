from django.db import models
from django.contrib.auth.models import User

class User_name(models.Model):
    firstname = models.CharField(null=False, max_length=255)
    secondname = models.CharField(null=False, max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='user_names')

    class Meta:
        verbose_name = 'User_name'
        verbose_name_plural = 'User_names'


class User_birth(models.Model):
    date_of_birth = models.DateField(null=True)
    place_of_birth = models.CharField(null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    user_name = models.ForeignKey(User_name, on_delete=models.CASCADE, null=False, related_name='user_births')

    class Meta:
        verbose_name = 'User_birth'
        verbose_name_plural = 'User_births'


class User_info(models.Model):
    specialization = models.CharField(null=False, max_length=255)
    orga_of_education =  models.CharField(null=False, max_length=255)
    year_of_graduation = models.IntegerField(null=False, default=False)
    user_name = models.ForeignKey(User_name, on_delete=models.CASCADE, null=False, related_name='user_infos')

    class Meta:
        verbose_name = 'User_info'
        verbose_name_plural = 'User_infos'

class User_work(models.Model):
    address = models.CharField(null=False, max_length=255)
    organization = models.CharField(null=False, max_length=255)
    user_name = models.OneToOneField(User_name, on_delete=models.CASCADE, null=False, related_name='user_works')


    class Meta:
        verbose_name = 'User_work'
        verbose_name_plural = 'User_works'

