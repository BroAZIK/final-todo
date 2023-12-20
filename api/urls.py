from django.urls import path

from .views import TaskView, TaskDetailView, LoginView

from rest_framework.authtoken.views import obtain_auth_token, ObtainAuthToken


urlpatterns = [
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
    path('login/', LoginView.as_view())
]