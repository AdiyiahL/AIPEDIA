# Generated by Django 4.2.4 on 2023-08-14 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='level',
            field=models.IntegerField(default=0, verbose_name='level'),
        ),
    ]
