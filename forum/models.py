# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Forum(models.Model):
    class Meta:
        db_table = "forum"
    forum_title = models.CharField(max_length=100)
    forum_description = models.TextField(default='No description provided.')
    forum_creator = models.ForeignKey(User, blank=True, null=True)
    forum_created = models.DateTimeField(auto_now=True)
    forum_updated = models.DateTimeField(auto_now=True)

    def num_posts(self):
        return sum([topic.num_posts() for topic in self.topic_set.all()])

    def last_post(self):
        if self.topic_set.count():
            last_post = None
            for topic in self.topic_set.all():
                post = topic.last_post()
                if post:
                    if not last_post:
                        last_post = post
                    elif post.created > last_post.created:
                        last_post = post
            return last_post


class Topic(models.Model):
    class Meta:
        db_table = "topic"
    topic_title = models.CharField(max_length=100)
    topic_description = models.TextField(default='No description provided.')
    topic_forum = models.ForeignKey(Forum)
    topic_creator = models.ForeignKey(User, blank=True, null=True)
    topic_created = models.DateTimeField(auto_now=True)
    topic_updated = models.DateTimeField(auto_now=True)
    closed = models.BooleanField(default=False)

    def num_posts(self):
        return self.post_set.count()

    def num_replies(self):
        return max(0, self.post_set.count() - 1)

    def last_post(self):
        if self.post_set.count():
            return self.post_set.order_by("post_created")[0]


class Post(models.Model):
    class Meta:
        db_table = "post"
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    post_creator = models.ForeignKey(User, blank=True, null=True)
    post_created = models.DateTimeField(auto_now_add=True)
    post_updated = models.DateTimeField(auto_now=True)
    post_topic = models.ForeignKey(Topic)
    post_user_ip = models.GenericIPAddressField(blank=True, null=True)

    def short(self):
        return u"%s - %s\n%s" % \
               (self.post_creator, self.post_title, self.post_created.strftime("%b %d, %I:%M %p"))

    short.allow_tags = True
