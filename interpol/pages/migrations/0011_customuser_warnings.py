# Generated by Django 4.0 on 2022-11-22 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_customuser_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='warnings',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
