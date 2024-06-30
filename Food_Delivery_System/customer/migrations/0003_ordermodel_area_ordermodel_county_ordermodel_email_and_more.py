# Generated by Django 5.0.6 on 2024-05-30 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_rename_orderitem_ordermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='area',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='county',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='email',
            field=models.EmailField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='second_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='sub_county',
            field=models.CharField(default='', max_length=30),
        ),
    ]
