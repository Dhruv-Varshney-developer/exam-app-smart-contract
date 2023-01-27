from django.urls import path
from . import views

urlpatterns = [
    path('',views.question, name="question"),
    path('home',views.home,name="home"),
    path('sign-up',views.sign_up,name="sign-up"),
    path('question',views.question,name="question")
]
