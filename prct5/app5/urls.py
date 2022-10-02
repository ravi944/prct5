from django.urls import path

from app5 import views
from app5.models import test
urlpatterns = [
    path('',views.index),
]