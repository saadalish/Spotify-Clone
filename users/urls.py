from django.urls import path

from users.views import (
    SignupView,
    UserLoginView,
    UserLogoutView
)

urlpatterns = [
    path('signup/', SignupView.as_view(), name="signup"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout")

]
