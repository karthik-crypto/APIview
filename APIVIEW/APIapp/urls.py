from django.urls import path
from APIapp import views

urlpatterns=[
path('hello-view/',views.helloAPIView.as_view()),
<<<<<<< HEAD
path('post',views.postAPIView.as_view()),
=======
>>>>>>> d0b074be15ea8067bf84f0f8ebb846ca94a751dd
]