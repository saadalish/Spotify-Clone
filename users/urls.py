from django.urls import path

import users.views

urlpatterns = [
    path('signup/', users.views.signup, name="signup"),
    path('login/', users.views.user_login, name="login"),
    path('logout/', users.views.user_logout, name="logout")

]
