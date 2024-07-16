from django.urls import path
from .views import HomePageView
from .views import AboutPageView
from .views import AccountPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("accounts", AccountPageView.as_view(), name="accounts")
]