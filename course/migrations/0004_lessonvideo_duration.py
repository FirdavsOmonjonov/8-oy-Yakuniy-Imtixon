# Generated by Django 5.0.6 on 2024-06-11 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_category_remove_lesson_video_alter_lesson_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonvideo',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
