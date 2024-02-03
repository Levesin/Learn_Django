from django.urls import path, include
from apps.first_example import views

app_name = "first_example"


urlpatterns = [
    path(
        "users/",
        include(
            [
                path("", views.UsersView.as_view(), name="users"),
                path("<int:amount>", views.UsersView.as_view(), name="users"),
            ]
        ),
    ),
]
