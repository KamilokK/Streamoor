# Generated by Django 2.1.4 on 2018-12-18 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0003_auto_20181218_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='streamooruser',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='streamooruser',
            name='email',
        ),
    ]