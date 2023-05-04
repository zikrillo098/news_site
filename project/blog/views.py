from django.shortcuts import render, redirect
from .models import Article, Category, CustomUser
from .forms import ArticleForm, LoginForm, CustomUserRegister
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


class ArticleList(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    extra_context = {
        'title': 'Главная страница'
    }

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class ArticleListByCategory(ArticleList):

    def get_queryset(self):
        return Article.objects.filter(
            category_id=self.kwargs['pk'], is_published=True
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = f'Категория :: ' + str(context['articles'][0].category)
        return context


class ArticleDetail(DetailView):
    model = Article

    def get_queryset(self):
        return Article.objects.filter(pk=self.kwargs['pk'], is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = Article.objects.get(pk=self.kwargs['pk'])
        article.watched += 1
        article.save()
        context['title'] = f'Статья :: {article.title}'
        articles = Article.objects.all()
        articles = articles.order_by('-watched')[:4]
        context['articles'] = articles
        return context


class NewArticle(CreateView):
    form_class = ArticleForm
    template_name = 'blog/article_form.html'
    success_url = 'index'
    extra_context = {
        'title': 'Добавить статью'
    }

    def form_valid(self, form):
        form.insstance.author = self.request.user
        return super().form_valid(form)


class SearchResults(ArticleList):
    def get_queryset(self):
        word = self.request.GET.get('q')
        articles = Article.objects.filter(
            Q(title__icontains=word) | Q(content__icontains=word), is_published=True
        )
        return articles


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy("index")
    context_object_name = 'article'


def profile(request, user_id):
    user = CustomUser.objects.get(pk=user_id)

    articles = Article.objects.filter(author=user)
    articles = articles.order_by('-watched')

    context = {
        'title': f'Страница пользователя :: {user.username}',
        'articles': articles,
        'user': user
    }
    return render(request, 'blog/profile.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()

    context = {
        'title': 'Авторизация пользователя',
        'form': form
    }
    return render(request, 'blog/login_form.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == "POST":
        form = CustomUserRegister(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = CustomUserRegister()

    context = {
        'title': 'Регистрационная панель',
        'form': form
    }
    return render(request, 'blog/register.html', context)


class ProfileUpdate(UpdateView):
    model = CustomUser
    form_class = CustomUserRegister
    template_name = 'blog/register.html'

