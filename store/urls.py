from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("about/", views.about, name="about"),
    path("product/<int:pk>/", views.product, name="product"),
    path("category/<str:category_title>/", views.category, name="category"),
    path("category_summary/", views.category_summary, name="category_symmary"),
]
