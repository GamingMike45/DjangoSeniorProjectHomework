from django.urls import path
from . import views

app_name="tasks"

urlpatterns = [
    path("listnotifications", views.list_notifications, name="list_notifications"),
    path("listnotifications/<str:username>", views.list_user_notifications, name="list_user_notifications"),
]