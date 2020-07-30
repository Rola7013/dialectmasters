from django.urls import path
from .views import indexView, challengesView, challenge_detail, post_user_detail, know_view, check_answers

app_name = 'retos'

urlpatterns = [
    path('index/', indexView, name='index'),
    path('list/', challengesView, name='list'),
    path('detail/<int:pk>/', challenge_detail, name='challenges_detail'),
    path('user/detail/<int:pk>/', post_user_detail, name='post_user_detail'),
    path('check/answers/<slug:slug>/', check_answers, name='check_answers'),
    path('know/', know_view, name='know'),
]