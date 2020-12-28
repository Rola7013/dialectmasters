from rest_framework import routers, permissions
from .api import *

from django.urls import path

app_name = 'api'

urlpatterns = [
	path('api/users/login', CustomObtainAuthToken.as_view()),
]


router = routers.DefaultRouter()
router.register('api/users', UserViewSet, 'api')
router.register('api/language_learning', Language_learningViewSet, 'api')
router.register('api/language_native', Language_nativeViewSet, 'api')
router.register('api/challenge', ChallengeViewSet, 'api')
router.register('api/postuser', PostUserViewSet, 'api')
router.register('api/answerchallenge', AnswerChallengeViewSet, 'api')
router.register('api/comment', CommentViewSet, 'api')

urlpatterns += router.urls