# Generated by Django 5.0.6 on 2024-06-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_sendmessage_delete_sendmassege'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendMassage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='SendMessage',
        ),
    ]
