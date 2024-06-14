from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, CourseViewSet, LessonViewSet, UserCommentsViewSet, 
    LessonVideoViewSet, Filter, SendMassageAPIView, LikeAPIView
)

router = DefaultRouter()
# Kurslarni kategoriyasi uchun urls
router.register('category-course', CategoryViewSet)
# Kurslar uchun urls
router.register('course-list', CourseViewSet)
# Darslar uchun urls
router.register('lessons', LessonViewSet)
# Darslarni kommentariyasi uchun urls
router.register('user-comments', UserCommentsViewSet)
# Darslarga video yuklash uchun urls
router.register('lessons-video', LessonVideoViewSet)

urlpatterns = [
    # Filterlash uchun urls
    path('filter/', Filter.as_view()),
    # Foydalanuvchilarni emailiga yuborish uchun urls
    path('send-massege/', SendMassageAPIView.as_view()),
    # Darsga like bosish uchun urls
    path('like/', LikeAPIView.as_view()),
    # Routerlarga urls
    path('', include(router.urls)),
]
