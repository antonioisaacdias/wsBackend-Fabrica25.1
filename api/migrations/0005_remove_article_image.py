# Generated by Django 4.2.19 on 2025-03-01 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
    ]
