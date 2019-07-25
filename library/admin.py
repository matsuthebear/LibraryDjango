from django.contrib import admin

# Register your models here.
from .models import Book, LeaderBoard, Cart, Order

admin.site.register(Book)
admin.site.register(LeaderBoard)
admin.site.register(Cart)
admin.site.register(Order)
