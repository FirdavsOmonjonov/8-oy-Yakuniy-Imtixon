# Generated by Django 5.0.6 on 2024-06-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_sendmassege'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='SendMassege',
        ),
    ]
