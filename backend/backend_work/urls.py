from django.urls import path, re_path, include

from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'userDetails', views.ImgView, basename='userDetails')
router.register(r'FormView', views.FormView, basename='FormView')
router.register(r'post', views.PostView, basename='post')
router.register(r'comments', views.CommentsView, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    # path('test/', views.My_test),
]
