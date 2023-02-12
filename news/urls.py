from django.urls import path
from .views import NewsList, NewsSearch, NewsDetailView, NewsCreateView, NewsUpdateView, NewsDeleteView # импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', NewsList.as_view()),
    path('search', NewsSearch.as_view()),
    path('<int:pk>', NewsDetailView.as_view(), name='news'),
    path('add/', NewsCreateView.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
]