from rest_framework import serializers, response, status
from retos.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    safe_question = serializers.CharField(source='usuarios.safe_question')
    user_language_learning = serializers.CharField(source='usuarios.user_language_learning')
    second_user_language_learnin = serializers.CharField(source='usuarios.second_user_language_learnin')
    user_language_native = serializers.CharField(source='usuarios.user_language_native')
    date = serializers.DateField(source='usuarios.date')
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'email', 'last_name', 'safe_question', 'user_language_learning',
                  'second_user_language_learnin', 'user_language_native', 'date', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class Language_learningSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language_learning
        fields = '__all__'

class Language_nativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language_native
        fields = '__all__'

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'

class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostUser
        fields = '__all__'

class AnswerChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerChallenge
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'