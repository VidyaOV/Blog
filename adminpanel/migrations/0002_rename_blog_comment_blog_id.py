# Generated by Django 5.0.6 on 2024-07-08 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='blog',
            new_name='blog_id',
        ),
    ]
