# Generated by Django 2.2.2 on 2019-06-14 08:43

from django.db import migrations, models
import listApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('date', models.DateTimeField(verbose_name='date published')),
            ],
            managers=[
                ('objects', listApp.models.ItemManager()),
            ],
        ),
    ]
