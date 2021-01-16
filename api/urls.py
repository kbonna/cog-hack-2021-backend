from django.urls import path
from . import views

urlpatterns = [
    path("faces/", views.FaceView.as_view(), name="face_list"),
]