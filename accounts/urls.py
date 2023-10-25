from django.urls import path
from .views import SignUpView


urlpatters = [
    path("singup/", SignUpView.as_view(), name="signup"),
]