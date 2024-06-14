from rest_framework import serializers
from .models import Category, Course, UserComments, Lesson, LessonVideo, SendMassage, Like


class CategorySerializer(serializers.ModelSerializer):
    """Kategoriya uchun serializer"""
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """Kurs uchun serializer"""
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """Dars uchun serializer"""
    class Meta:
        model = Lesson
        fields = '__all__'


class UserCommentsSerializer(serializers.ModelSerializer):
    """Foydalanuvchi izohlari uchun serializer"""
    class Meta:
        model = UserComments
        fields = '__all__'


class LessonVideoSerializer(serializers.ModelSerializer):
    """Dars video uchun serializer"""
    class Meta:
        model = LessonVideo
        fields = '__all__'


class SendMassageSerializer(serializers.ModelSerializer):
    """Xabar yuborish uchun serializer"""
    class Meta:
        model = SendMassage
        fields = '__all__'


class LikeSerializer(serializers.Serializer):
    """Darsga ovoz berish uchun serializer"""
    Lesson = serializers.IntegerField()
    like = serializers.BooleanField()
    dislike = serializers.BooleanField()
