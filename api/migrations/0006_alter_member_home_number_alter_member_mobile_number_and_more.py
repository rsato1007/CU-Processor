# Generated by Django 4.0.5 on 2022-06-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_member_home_number_alter_member_mobile_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='home_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='mobile_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='work_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
