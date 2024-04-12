# polls 폴더에 urls.py가 업어서 새로 생성

from django.urls import path, re_path
from blog.models import Post
from blog.views import PostLV
from blog.views import PostDV
from blog.views import postArchiveView
from blog.views import postYearArchiveView
from blog.views import postMonthArchiveView

app_name = "blog"

urlpatterns = [
    path("", PostLV.as_view(), name="index"),
    re_path(r'post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name="post_detail"),
    path(
        "archive/",
        postArchiveView.as_view(model = Post,),
        name="post_archive",
    ),
    path(
        "<int:year>/",
          postYearArchiveView.as_view(),
            name="post_year_archive"
    ),

    # Example: /2012/08/
    path(
        "<int:year>/<int:month>/",
        postMonthArchiveView.as_view(month_format="%m"),
        name="post_month_numeric",
    ),
    # Example: /2012/aug/
    path(
        "<int:year>/<str:month>/",
        postMonthArchiveView.as_view(),
        name="post_month",
    ),
]