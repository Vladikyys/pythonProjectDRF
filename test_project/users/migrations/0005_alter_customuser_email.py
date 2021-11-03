# Generated by Django 3.2.8 on 2021-11-03 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=100, null=True, unique=True, verbose_name='email'),
        ),
    ]
