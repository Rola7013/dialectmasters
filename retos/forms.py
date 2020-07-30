from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import Usuarios, PostUser, AnswerChallenge, Comment
from django.contrib.auth.models import User
from mptt.forms import TreeNodeChoiceField
from django import forms


class UserForm(ModelForm):
    class Meta:
        model = Usuarios

        fields = ('safe_question', 'user_language_learning', 'user_language_native', 'second_user_language_learnin')

class EditUserForm(UserChangeForm):
    class Meta:
        model = Usuarios

        fields = ( 'second_user_language_learnin', 'password',)

class PostUserForm(ModelForm):
    class Meta:
        model = PostUser
        fields = ('answer', 'voice',)

class AnswerChallengeForm(ModelForm):
    class Meta:
        model = AnswerChallenge
        fields = ('text', )

    def __init__(self, *args, **kwargs):
        super(AnswerChallengeForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs={
            'id': 'pasteArea',
        }
        self.fields['text'].widget.attrs = {
            'id': 'pasteArea',
        }


class NewCommentForm(ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update(
            {'class': 'd-none'})
        self.fields['parent'].label = ''
        self.fields['parent'].required = False

    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def save(self, *args, **kwargs):
        Comment.objects.rebuild()
        return super(NewCommentForm, self).save(*args, **kwargs)