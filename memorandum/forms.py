from django import forms
from .models import Article
from .models import Tag


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "body", "tags"]  # 正しいフィールドを指定


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
