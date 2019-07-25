from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models import Sum
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(blank = True, null = True, upload_to = 'book_picture')
    author = models.CharField(max_length = 100)
    publisher = models.CharField(max_length = 100)
    year = models.IntegerField(default = 0)
    isbn = models.CharField(max_length = 13)
    genre = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length = 500)
    units_sold = models.IntegerField(default = 0)
    points = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.title} - {self.author}'


class LeaderBoard(models.Model):
    position = models.IntegerField()
    genre = models.CharField(max_length = 100)
    book = models.OneToOneField(Book, on_delete = models.CASCADE, default = 1)
    many_weeks = models.IntegerField()

    def __str__(self):
        return f' Position : {self.position} - Genre : {self.genre} - Book : {self.book}'

class Order(models.Model):
    PAYMENT_CHOICES = (
        ('P' , 'PAYPAL'),
        ('C' , 'CREDIT CARD'),
        ('M' , 'MARK'),
    )
    STATUS_ORDER = (
        ('K' , 'PAYED'),
        ('D' , 'DELIVERED'),
        ('R' , 'RETURNED'),
    )
    date = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField(Book)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    total_cost = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    payment = models.CharField(max_length = 1, choices = PAYMENT_CHOICES)
    status = models.CharField(max_length = 1, choices = STATUS_ORDER, default = 'K')
    points = models.IntegerField(default = 1)
    address = models.CharField(max_length = 100, default = None, blank = True, null=True)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    books = models.ManyToManyField(Book, default = None, blank = True)
    def __str__(self):
        return f'{self.user} - Cart'
    def get_price(self):
        return (self.books.aggregate(Sum('price'))['price__sum'] or 0.00)
