from django.db import models
from django.contrib.auth.models import User
from library.models import Book
#from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    code = models.CharField(max_length = 10)
    city = models.CharField(max_length = 100)
    telephone = models.CharField(max_length = 10)

    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        if self.user.is_superuser:
            return self.user.username + '- ADMIN'
        else :
            return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class BookCard(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    emission_date = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default = 0)

    def __str__(self):
        if self.user.is_superuser:
            return self.user.username + '- ADMIN CARD'
        else :
            return self.user.username + '- CARD'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
