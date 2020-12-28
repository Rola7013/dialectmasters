from .validators import validate_file_extension
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from stdimage import StdImageField, JPEGField



from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.


class Language_learning(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Language_native(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    safe_question = models.CharField(max_length=200)
    user_language_learning = models.ForeignKey(Language_learning, on_delete=models.CASCADE, blank=False, null=True)
    second_user_language_learnin = models.ForeignKey(Language_learning, related_name='second_language', on_delete=models.CASCADE, blank=True, null=True)
    user_language_native = models.ForeignKey(Language_native, on_delete=models.CASCADE, blank=False, null=True)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Usuarios.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.usuarios.save()



class Challenge(models.Model):
    user_language_learning = models.ForeignKey(Language_learning, on_delete=models.CASCADE, blank=False, null=True)
    title = models.CharField(max_length=100)
    description = RichTextField()
    date = models.DateField(auto_now_add=True)
    image = StdImageField(upload_to='imag_retos',
                          variations={'thumbnail': {'width': 100, 'height': 75}})


    def __str__(self):
        return "{}".format(self.title)

class PostUser(models.Model):
    user_language_native = models.ForeignKey(Language_native, on_delete=models.CASCADE, blank=False, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='post_user')
    answer = RichTextField()
    date = models.DateField(auto_now_add=True)
    voice = models.FileField(upload_to='imag_retos', validators=[validate_file_extension], blank=True)

    def __str__(self):
        return "Post de {}".format(self.user)

class AnswerChallenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, blank=True, null=True)
    postuser = models.ForeignKey(PostUser, on_delete=models.CASCADE, related_name='answer_post_user')
    slug = models.SlugField(default=True, max_length=250, unique_for_date='date')
    text = RichTextField()
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return "Answer from {} from the challenge {}".format(self.user, self.challenge)

    def get_absolute_url(self):
        return reverse('retos:check_answers', args=[self.slug])

class Comment(MPTTModel):
    article = models.ForeignKey(AnswerChallenge, on_delete=models.CASCADE, related_name='comments' , null=True, blank=True)
    user = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['created']

    def __str__(self):
        return self.body[:20]
