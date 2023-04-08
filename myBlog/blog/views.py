#  Mohamed Essam Abdelfattah Copyright (c) 2023.

from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView

from .models import Post


# Create your views here.

class AboutView(TemplateView):
    template_name = "about.html"


class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_data__lte=timezone.now()).order_by("-published_date")


class PostDetails(DetailView):
    template_name = "PostDetails.html"
