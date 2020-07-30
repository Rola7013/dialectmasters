from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Usuarios, Challenge, PostUser, AnswerChallenge, Comment
from .forms import UserForm, PostUserForm, AnswerChallengeForm, EditUserForm, NewCommentForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def create_user(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        usuario_form = UserForm(request.POST)

        if user_form.is_valid() and usuario_form.is_valid():
            user = user_form.save()
            usuario = usuario_form.save(commit=False)
            usuario.user = user
            usuario.save()
            return redirect('retos:login')

    else:
        user_form = UserCreationForm()
        usuario_form = UserForm()

    return render(
        request,
        'registration.html',
        {'user_form': user_form, 'usuario_form': usuario_form}
    )


@login_required
def indexView(request):
    return render(request, 'index.html', {})

def know_view(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user.usuarios)
        if user_form.is_valid():
            user_form.save()
            return redirect('retos:index')

    else:
        user_form = EditUserForm(instance=request.user)

    return render(request, 'know.html', {'user_form': user_form})

def challengesView(request):
    template = 'challenges.html'
    post_users = PostUser.objects.filter(date__lte=timezone.now()).order_by('date')
    challenges = Challenge.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, template, {'challenges': challenges,
                                      'post_users': post_users})

def challenge_detail(request, pk):
    template = 'challenges_detail.html'
    challenge = get_object_or_404(Challenge, pk=pk)

    new_post = None
    if request.method == 'POST':
        post_user_form = PostUserForm(request.POST, request.FILES)
        if post_user_form.is_valid():
            new_post = post_user_form.save(commit=False)
            new_post.challenge = challenge
            new_post.user = request.user
            new_post.save()

            return redirect('retos:list')

    else:
        post_user_form = PostUserForm()

    return render(request, template, {'challenge': challenge,
                                        'new_post': new_post,
                                        'post_user_form': post_user_form,

    })

def post_user_detail(request, pk):
    template = 'post_user_detail.html'
    post_users = get_object_or_404(PostUser, pk=pk)
    challenge = post_users.challenge
    comments = post_users.answer_post_user.filter()
    new_answer = None
    if request.method == 'POST':
        answer_challenge_form = AnswerChallengeForm(data=request.POST)
        if answer_challenge_form.is_valid():
            new_answer = answer_challenge_form.save(commit=False)
            new_answer.challenge = challenge
            new_answer.user = request.user
            new_answer.postuser = post_users
            new_answer.save()

    else:
        answer_challenge_form = AnswerChallengeForm()


    return render(request, template, {'challenge': challenge,
                                      'post_users': post_users,
                                      'comments': comments,
                                      'new_answer': new_answer,
                                      'answer_challenge_form': answer_challenge_form,
                                      })


def check_answers(request, slug):
    template = 'check_answers.html'
    answers = get_object_or_404(AnswerChallenge, slug=slug)
    allcomments = answers.comments.filter(status=True)
    page = request.GET.get('page', 1)

    paginator = Paginator(allcomments, 10)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    challenge = answers.challenge
    post_users = answers.postuser

    user_comment = None
    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)

        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.article = answers
            user_comment.user = request.user.usuarios
            user_comment.save()

            return redirect('retos:list')
    else:
        comment_form = NewCommentForm()

    context = {
        'comment_form': comment_form,
        'answers': answers,
        'post_users': post_users,
        'challenge': challenge,
        'allcomments': allcomments,
        'comments': user_comment,
        'comments': comments,
    }

    return render(request, template, context)






