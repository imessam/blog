"""myBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import *

urlpatterns = [
    path("", PostList.as_view(), name="PostList"),
    path("about/", AboutView.as_view(), name="About"),
    path("post/<int:pk>", PostDetails.as_view(), name="PostDetails"),
    path("post/add",PostCreate.as_view(), name = "PostAdd"),
    path("post/<int:pk>/publish",postPublish,name = "PostPublish"),
    path("post/<int:pk>/edit", PostUpdate.as_view(), name = "PostEdit"),
    path("post/<int:pk>/delete", PostDelete.as_view(), name = "PostDelete"),
    path("post/<int:pk>/comment/add", commentAdd,name = "CommentAdd"),
    path("comment/<int:pk>/approve",commentApprove, name = "CommentApprove"),
    path("comment/<int:pk>/delete",commentDelete, name = "CommentDelete")

]
