# Generated by Django 5.0.6 on 2024-06-14 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_remove_usercomments_mark_like'),
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
    ]
