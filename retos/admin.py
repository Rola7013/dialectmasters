from django.contrib import admin
from .models import Usuarios, Language_native, Language_learning, Challenge, PostUser, AnswerChallenge, Comment
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from mptt.admin import MPTTModelAdmin

class Language_native_admin(admin.ModelAdmin):
    fields = ('title',)
    list_display = ('title',)

admin.site.register(Language_native, Language_native_admin)


class Language_learning_admin(admin.ModelAdmin):
    fields = ('title',)
    list_display = ('title',)

admin.site.register(Language_learning, Language_learning_admin)

class UsuariosInLink(admin.StackedInline):
    model = Usuarios
    can_delete = False
    verbose_name_plural = 'usuarios'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UsuariosInLink,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class ChallengeAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'description',
        'image',
        'user_language_learning',
    )
    list_display = ('title', 'date', 'user_language_learning')
    list_filter = ('title', 'date', 'user_language_learning')

admin.site.register(Challenge, ChallengeAdmin)


class PostUserAdmin(admin.ModelAdmin):
    fields = (
        'user',
        'challenge',
        'answer',
        'voice',
        'user_language_native',

    )

    list_display = ('user', 'challenge', 'user_language_native',)
    list_filter = ('date', 'user_language_native',)

admin.site.register(PostUser, PostUserAdmin)


class AnswerChallengeAdmin(admin.ModelAdmin):
    fields = ('user', 'text', 'challenge', 'postuser', )

    list_display = ('user', 'challenge', 'postuser', 'date', 'slug', )

    list_filter = ('date', 'challenge', 'postuser', )

admin.site.register(AnswerChallenge, AnswerChallengeAdmin)


admin.site.register(Comment, MPTTModelAdmin)