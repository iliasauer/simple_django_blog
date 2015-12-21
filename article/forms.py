from django.forms import ModelForm

from article.models import Commentary


class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ['commentary_text']
