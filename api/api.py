from retos.models import *
from .serializers import *
from rest_framework import viewsets, status
from django.shortcuts import render
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        return Response({
            'user_id': user.pk,
            'email': user.email,
            'username': user.username
        })


class Language_learningViewSet(viewsets.ModelViewSet):
    queryset = Language_learning.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = Language_learningSerializer

class Language_nativeViewSet(viewsets.ModelViewSet):
    queryset = Language_native.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = Language_nativeSerializer

class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = ChallengeSerializer

class PostUserViewSet(viewsets.ModelViewSet):
    queryset = PostUser.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = PostUserSerializer

class AnswerChallengeViewSet(viewsets.ModelViewSet):
    queryset = AnswerChallenge.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = AnswerChallengeSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = CommentSerializer