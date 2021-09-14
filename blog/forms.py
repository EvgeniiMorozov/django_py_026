from django.forms import ModelForm, TextInput, Textarea

from .models import PostModel


class PostForm(ModelForm):
    class Meta:
        model = PostModel
        fields = ('author', 'title', 'text')
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор статьи',
                'id': 'authorArticle'
            }),
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
                'id': 'titleArticle'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'id': 'textArticle',
                'rows': '3',
                'placeholder': 'Текст статьи',
            }),
        }
