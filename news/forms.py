from django.forms import ModelForm, BooleanField
from .models import Post


# Создаём модельную форму
class NewsForm(ModelForm):
    class Meta:
        model = Post
        fields = ['header', 'authorArticle', 'postText']