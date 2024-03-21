from django.urls import path, include, re_path
from rest_framework import routers
from courses import views

r = routers.DefaultRouter()
r.register('categories', views.CategoryViewset, basename='categories')
r.register('courses', views.CourseViewset, basename='courses')
r.register('lessons', views.LessonViewset, basename='lessons')
r.register('users', views.UserViewset, basename='users')

urlpatterns = [
    path('', include(r.urls))
]
