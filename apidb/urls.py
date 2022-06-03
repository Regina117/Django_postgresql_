from django.urls import path
from .views import DBAPIView
urlpatterns = [
        path('', DBAPIView.as_view()),
]