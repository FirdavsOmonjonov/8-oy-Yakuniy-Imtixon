# Generated by Django 5.0.6 on 2024-06-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_usercomments_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercomments',
            name='mark',
            field=models.IntegerField(max_length=5),
        ),
    ]
