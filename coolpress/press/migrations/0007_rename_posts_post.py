# Generated by Django 3.2.7 on 2022-11-15 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0006_rename_post_posts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]
