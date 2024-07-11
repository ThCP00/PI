from django.urls import path
from blog import views

urlpatterns = [
	
	path("dashboard/", views.dashboard, name="dashboard"),
	path("blog/", views.blog, name="blog"),
	path("comentario/", views.comentario, name="comentario"),
]
