from django.urls import path
from APIapp import views

urlpatterns=[
path('hello-view/',views.helloAPIView.as_view()),
]