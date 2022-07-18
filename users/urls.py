from django.urls import path
from rest_framework.authtoken import views

from users.views import RegisterUserAPIView

urlpatterns = [
    path('signup/', RegisterUserAPIView.as_view(), name="signup"),
    path('login/', views.obtain_auth_token)

]
