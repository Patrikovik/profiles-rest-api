from django.urls import path

from profiles_api_2 import views


urlpatterns = [
    path('hello-view',views.HelloApiView.as_view()),
]
