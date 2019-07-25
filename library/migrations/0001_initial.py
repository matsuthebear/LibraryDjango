# Generated by Django 2.2.3 on 2019-07-25 04:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='book_picture')),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('year', models.IntegerField(default=0)),
                ('isbn', models.CharField(max_length=13)),
                ('genre', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.CharField(max_length=500)),
                ('units_sold', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('payment', models.CharField(choices=[('P', 'PAYPAL'), ('C', 'CREDIT CARD'), ('M', 'MARK')], max_length=1)),
                ('status', models.CharField(choices=[('K', 'PAYED'), ('D', 'DELIVERED'), ('R', 'RETURNED')], default='K', max_length=1)),
                ('points', models.IntegerField(default=1)),
                ('address', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('books', models.ManyToManyField(to='library.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeaderBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('many_weeks', models.IntegerField()),
                ('book', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='library.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.ManyToManyField(blank=True, default=None, to='library.Book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
