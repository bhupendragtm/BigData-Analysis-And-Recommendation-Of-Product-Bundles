from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.Register,name="register"),
    path('login/',views.Login,name="login"),
    path('logout/',views.Logout,name="logout")
]
