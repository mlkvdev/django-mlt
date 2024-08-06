from django.urls import path
from rest_framework import routers

from app import views

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogViewSet)
router.register(r'comments', views.CommentViewSet)
urlpatterns = [
    path('test/', views.TestAPIView.as_view()),
    path('error/', views.ErrorAPIView.as_view()),
    path('raise-error/', views.RaiseErrorAPIView.as_view()),
]
urlpatterns += router.urls
