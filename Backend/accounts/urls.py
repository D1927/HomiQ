from django.urls import path
from .views import RegisterView , LoginView

urlpatterns = [ # All urls that can be used
    path("register/", RegisterView.as_view(), name="register"), # "register/" --- url with that startpoint , ".as_view()" --- we use it to call a class , name for using this particular again in code somewhere
    path("login/", LoginView.as_view(), name="login"),
]