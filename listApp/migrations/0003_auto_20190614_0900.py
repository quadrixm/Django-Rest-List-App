# Generated by Django 2.2.2 on 2019-06-14 09:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listApp', '0002_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='uploads'),
            preserve_default=False,
        ),
    ]
