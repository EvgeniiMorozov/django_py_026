from django.forms import ModelForm, TextInput, Textarea, SlugField

from .models import PostModel


# Class Based Forms (CBF)
class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].label = 'Автор статьи'
        self.fields['title'].label = 'Название статьи'
        self.fields['text'].label = 'Текст статьи'
        self.fields['slug'].label = 'URL статьи'
        self.label_suffix = ""
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = PostModel
        fields = ['author', 'title', 'slug', 'text', 'image', 'category']
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите автора статьи',
                'id': 'author-input'
            }),
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название статьи',
                'id': 'title-input'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст статьи',
                'id': 'text-input'
            }),
            'slug': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите URL статьи (необязательно)',
                'id': 'slug-input'
            })
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            self.add_error('title', 'Больше 50 символов!')
        if '!!' in title:
            self.add_error('title', 'Очень много восклицательных знаков!!!')
        return title
