# from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView,DeleteView
from .models import Post
from .filters import NewsFilter
from .forms import NewsForm


class NewsList(ListView):
    model = Post
    template_name = 'news_list.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'newsall'
    queryset = Post.objects.order_by('-creationTime')
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NewsForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не накосячил, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)

class NewsSearch(ListView):
    model = Post
    template_name = 'search.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'newsSearch'
    queryset = Post.objects.order_by('-creationTime')
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET,
        queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context


# дженерик для получения деталей о товаре
class NewsDetailView(DetailView):
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.all()



# дженерик для создания объекта. Надо указать только имя шаблона и класс формы который мы написали в прошлом юните. Остальное он сделает за вас
class NewsCreateView(CreateView):
    template_name = 'news_create.html'
    form_class = NewsForm


# дженерик для редактирования объекта
class NewsUpdateView(UpdateView):
    template_name = 'news_create.html'
    form_class = NewsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class NewsDeleteView(DeleteView):
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'