from django import forms
from .models import Article, CustomUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'photo',
            'is_published',
            'category'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Название',
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Описание',
                'class': 'form-control'
            }),
            'photo': forms.FileInput(attrs={
                'placeholder': 'Изоброжение',
                'class': 'form-control'
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))


class CustomUserRegister(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтвердите пароль'
    }))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Эмэйл'
    }))
    phone_number = forms.CharField(required=False, max_length=15, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Номер'
    }))
    first_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя'
    }))
    last_name = forms.URLField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Фамилия'
    }))
    site_link = forms.URLField(required=False, widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ссылка на сайт'
    }))
    instagram_link = forms.URLField(required=False, widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ссылка на инстаграм'
    }))
    twitter_link = forms.URLField(required=False, widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ссылка на ваш сайт'
    }))
    github = forms.URLField(required=False, max_length=100, widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'GIT_HUB'
    }))
    facebook_link = forms.URLField(required=False, widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ссылка на фэйсбук'
    }))
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Адресс'
    }))
    photo = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = CustomUser
        fields = ('first_name',
                  'last_name',
                  'site_link',
                  'username',
                  'email',
                  'phone_number',
                  'password1',
                  'password2',
                  'instagram_link',
                  'twitter_link',
                  'facebook_link',
                  'address',
                  'github',
                  'photo')
