from django.urls import path
from APIapp import views

urlpatterns=[
path('hello-view/',views.helloAPIView.as_view()),
<<<<<<< HEAD
path('post',views.postAPIView.as_view()),
]
=======

path('post',views.postAPIView.as_view()),

]
>>>>>>> 7c9de4e82d545c51d6bece2aacb82e437103b011
