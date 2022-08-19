from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import FeedBackForm
from django.contrib import messages

# Create your views here.


class MainPage(ListView):
    model = Articles
    template_name = 'MainApp/MainPage.html'
    context_object_name = 'Articles'
    allow_empty = False

    def get_queryset(self):
        return Articles.objects.filter(is_published=True)


class ArticlePage(DetailView):
    model = Articles
    template_name = 'MainApp/ArticlePage.html'
    context_object_name = 'Article'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Articles.objects.get(pk=self.kwargs['pk'])
        return context


class FeedBackPage(CreateView):
    form_class = FeedBackForm
    template_name = 'MainApp/FeedBackPage.html'
    success_url = reverse_lazy('main_page')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def post(self, request):
        if request.method == "POST":
            form = FeedBackForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Вопрос успешно отправлен")
                return redirect('feedback_page')
            else:
                messages.error(request, "Произошла ошибка")
                form = FeedBackForm()
                return redirect('feedback_page')
