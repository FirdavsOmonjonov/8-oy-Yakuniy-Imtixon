from django.contrib import admin
from .models import Category, Course, UserComments, Lesson, LessonVideo, Like, SendMassage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'quantity', 'price')
    list_display_links = ('id', 'name',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course', 'description')
    list_display_links = ('id', 'name',)


@admin.register(UserComments)
class UserCommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'lesson', 'message', 'add_time')
    list_display_links = ('id', 'user',)


@admin.register(LessonVideo)
class LessonVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'video', 'duration')
    list_display_links = ('id', 'lesson',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'lesson', 'like_or_dislike')
    list_display_links = ('id', 'user',)


@admin.register(SendMassage)
class SendMassageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'message')
    list_display_links = ('id', 'name',)
