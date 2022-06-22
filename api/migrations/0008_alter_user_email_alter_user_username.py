# Generated by Django 4.0.5 on 2022-06-22 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_user_staff_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
