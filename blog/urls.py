from django.urls import path
from blog import views

urlpatterns = [
	path("", views.home, name="home"),
	path("dashboard/", views.dashboard, name="dashboard"),
	path("blog/", views.blog, name="blog"),
]
