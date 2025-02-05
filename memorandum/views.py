from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import generic
from django.views.generic import CreateView, DetailView
from .models import Article
from .forms import ArticleForm  # type: ignore
from .models import Tag, Article
from .forms import TagForm


class ArticleListView(generic.ListView):
    model = Article

    # 参照するhtmlファイルを指定
    template_name = "memorandum/index.html"


class ArticleDetailView(generic.DetailView):
    model = Article
    # 参照するhtmlファイルを指定
    template_name = "memorandum/detail.html"


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "memorandum/create.html"


class ArticleUpdateView(generic.edit.UpdateView):
    model = Article
    fields = ["title", "tag", "body"]
    # 参照するhtmlファイルを指定
    template_name = "memorandum/update.html"
    success_url = reverse_lazy("memorandum:index")  # POSTが正しく行われた際に飛ばすURL


class ArticleDeleteView(generic.edit.DeleteView):
    model = Article
    # 参照するhtmlファイルを指定
    template_name = "memorandum/delete.html"
    success_url = reverse_lazy("memorandum:index")  # POSTが正しく行われた際に飛ばすURL


class TagCreateView(generic.edit.CreateView):
    model = Tag
    fields = ["name"]
    # 参照するhtmlファイルを指定
    template_name = "memorandum/create-tag.html"
    success_url = reverse_lazy("memorandum:index")  # POSTが正しく行われた際に飛ばすURL


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "memorandum/create.html"

    def get_success_url(self):
        return reverse_lazy("memorandum:detail", kwargs={"pk": self.object.pk})


class ArticleDetailView(DetailView):  # type: ignore
    model = Article
    template_name = "memorandum/detail.html"
