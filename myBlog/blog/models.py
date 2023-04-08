from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    createdDate = models.DateTimeField(timezone.now())
    publishDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publishDate = timezone.now()
        self.save()

    def approveComments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse(viewname="postDetails", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey("blog.Post", related_name="comments")
    author = models.CharField(max_length=200)
    text = models.TextField()
    createdDate = models.DateTimeField(timezone.now())
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def get_absolute_url(self):
        return reverse(viewname="postList")

    def __str__(self):
        return self.text
