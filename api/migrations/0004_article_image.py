# Generated by Django 4.2.19 on 2025-03-01 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='aticles_images/'),
        ),
    ]
