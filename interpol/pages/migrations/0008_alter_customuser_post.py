# Generated by Django 4.1.2 on 2022-10-28 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_comment_alter_customuser_id_alter_customuser_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='post',
            field=models.TextField(default='Administrator'),
        ),
    ]
