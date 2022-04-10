from django.db import models


class UserInfo(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    custom_url = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    is_private = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateTimeField(auto_now_add=True)

