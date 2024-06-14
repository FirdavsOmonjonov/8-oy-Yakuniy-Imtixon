from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from moviepy.editor import VideoFileClip
from django.utils import timezone
from django.dispatch import receiver
from datetime import timedelta


class Category(models.Model):
    """Online kurslar uchun kategoriyalar yaratish imkoniyatini beradi."""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    """Kurslarni yaratish uchun model, kursning nomi, haqida qisqacha izoh, davomiyligi, narxi va boshqa ma'lumotlarni saqlaydi"""
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses')
    description = models.CharField(max_length=225)
    duration = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Umumiy kurs narxi")

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """Kursga dars qo'shish imkoniyatini beradi, darsning nomi, haqida izoh va qaysi kursga bog'liqligini saqlaydi."""
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, help_text='Kurs nomi')

    def __str__(self):
        return self.name


class UserComments(models.Model):
    """Foydalanuvchilar tomonidan darslar uchun qoldirilgan izohlarni saqlaydi."""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.lesson} - {self.user}'


def file_size(value):
    """Bu method darslarga yuklanayotgan videolarni hajmiga jeklov qo'yishimizga yordam beradi"""
    limit = 300 * 1024 * 1024  
    if value.size > limit:
        raise ValidationError('Dars uchun yuklanayotgan video hajmi 300MB dan oshmasligi kerak')


class LessonVideo(models.Model):
    """Darslar uchun video yuklash imkoniyatini beradi, video faylini va uning davomiyligini saqlaydi."""
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, related_name='videos')
    video = models.FileField(
        upload_to='lesson/videos/',
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4', 'wmv']),
            file_size
        ]
    )
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f'{self.lesson.name} - {self.video.name}'


@receiver(post_save, sender=LessonVideo)
def save_video_duration(sender, instance, **kwargs):
    """Bu method darsga yuklanayotgan videolarni necha daqiqa ekani hisoblab beradi"""
    if instance.video and not instance.duration:
        video_path = instance.video.path
        video = VideoFileClip(video_path)
        duration_seconds = video.duration
        instance.duration = timedelta(seconds=duration_seconds)
        instance.save()


class Like(models.Model):
    """Foydalanuvchilar darslarga "like" yoki "dislike" qo'shish imkoniyatini beradi"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    like_or_dislike = models.BooleanField()

    def __str__(self):
        return f'{self.lesson} - {self.user}'


class SendMassage(models.Model):
    """Foydalanuvchilar orqali yuborilgan xabarlarni saqlash uchun model."""
    name = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.message}'
