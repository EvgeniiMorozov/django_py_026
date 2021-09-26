from django.forms import ModelForm, TextInput, Textarea
from django.core.exceptions import ValidationError

from .models import PostModel


class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'
    class Meta:
        model = PostModel
        fields = ('author', 'title', 'text', 'image')
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

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) > 10:
    #        raise ValidationError('To long title !!!')
    #     return title
