# Generated by Django 4.2.6 on 2023-10-27 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_message_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post/'),
        ),
    ]
