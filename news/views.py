from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import News_post
from .forms import News_postForm

def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})

@login_required
def create_news(request):
    error = ''
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            # Создание экземпляра News_post без сохранения в базу данных
            news_post = form.save(commit=False)
            # Установка текущего пользователя в качестве автора
            news_post.author = request.user
            # Сохранение экземпляра в базу данных
            news_post.save()
            return redirect('news_home')  # Убедитесь, что 'news_home' - это корректное имя URL
        else:
            error = 'Данные были заполнены некорректно'
    else:
        form = News_postForm()

    return render(request, 'news/add_news.html', {'form': form, 'error': error})