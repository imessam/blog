#  Mohamed Essam Abdelfattah Copyright (c) 2023.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post,Comment
from .forms import PostForm,CommentForm


# Create your views here.

class AboutView(TemplateView):
    template_name = "about.html"


class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_data__lte=timezone.now()).order_by("-published_date")


class PostDetails(DetailView):
    template_name = "blog/PostDetails.html"



class PostCreate(LoginRequiredMixin, CreateView):

    login_url = "/login/"
    redirect_field_name = "blog/PostDetails.html"
    model = Post
    form_class = PostForm


class PostUpdate(LoginRequiredMixin, UpdateView):

    login_url = "/login/"
    redirect_field_name = "blog/PostDetails.html"
    model = Post
    form_class = PostForm

class PostDelete(LoginRequiredMixin, DeleteView):

    model = Post
    success_url = reverse_lazy("blog/PostList.html")

@login_required
def postPublish(request,pk):

    post = get_object_or_404(Post,pk)
    post.publish()

    return redirect("PostDetails",pk = pk)



###################################################################
###################################################################


@login_required
def commentAdd(request,pk):

    post = get_object_or_404(Post,pk)
    if request.method == "POST":
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comment = CommentForm.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("PostDetails", pk = pk)
    else:
        commentForm = CommentForm()

    return render(request,"blog/CommentForm",{"commentForm":commentForm})


@login_required
def commentApprove(request,pk):

    comment = get_object_or_404(Comment,pk)
    comment.approve()

    return redirect("PostDetails",comment.post.pk)

@login_required
def commentDelete(request,pk):

    comment = get_object_or_404(Comment,pk)
    post_pk = comment.post.pk
    comment.delete()

    return redirect("PostDetails",post_pk)




