from django.forms import ModelForm

from forum.models import Post, Topic


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_title', 'topic_description']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_text']
