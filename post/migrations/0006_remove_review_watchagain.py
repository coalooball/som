# Generated by Django 4.2.2 on 2023-07-11 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_post_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='watchAgain',
        ),
    ]
