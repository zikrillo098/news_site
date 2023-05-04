from django.db import models
from django.urls import reverse
from django.core import validators
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Описание',
                               validators=[validators.MinLengthValidator(15, message='Мало ввели')])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='photo/', blank=True, null=True, verbose_name='Изображение')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    watched = models.IntegerField(default=0, verbose_name='Просмотры')
    author = models.ForeignKey('CustomUser', on_delete=models.PROTECT, default=None, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})

    def get_photo(self):
        if self.photo:
            return self.photo.url
        else:
            return 'https://avatars.mds.yandex.net/i?id=a85d135a5142f49ef1c5a4cd6aed1cebc97d8552-9181172-images-thumbs&n=13'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class CustomUser(AbstractUser):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'
    username = models.CharField(max_length=120, verbose_name='Имя пользователя', unique=True)
    first_name = models.CharField(max_length=20, verbose_name='Имя', blank=True, null=True)
    last_name = models.CharField(max_length=25, verbose_name='Фамилия', blank=True, null=True)
    email = models.EmailField(verbose_name='Почта', unique=True)
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    site_link = models.URLField(max_length=255, verbose_name='Ссылка на сайт')
    instagram_link = models.CharField(max_length=255, verbose_name='Ссылка на инстаграм', null=True, blank=True)
    twitter_link = models.CharField(max_length=255, verbose_name='Ссылка на твитер', null=True, blank=True)
    facebook_link = models.CharField(max_length=255, verbose_name='Ссылка на фэйсбук', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адресс')
    photo = models.ImageField(upload_to='profiles/', verbose_name='Фотография', blank=True, null=True)

    def get_photo(self):
        if self.photo:
            return self.photo.url
        else:
            return 'https://bootdey.com/img/Content/avatar/avatar7.png'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
