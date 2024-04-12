# polls 폴더에 urls.py가 업어서 새로 생성

from django.urls import path, re_path
<<<<<<< HEAD
from blog.models import Post
from blog.views import PostLV
from blog.views import PostDV
from blog.views import postArchiveView
from blog.views import postYearArchiveView
from blog.views import postMonthArchiveView
=======

from . import views
>>>>>>> upstream/main

app_name = "blog"

urlpatterns = [
<<<<<<< HEAD
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
=======
    path("", views.PostLV.as_view(), name="index"),    
    path("post/", views.PostLV.as_view(), name="post_list"),    
    # path("post/<slug:slug>", views.PostDV.as_view(), name="post_detail"),    
    re_path(r'post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name="post_detail"), 
    
    # Example: /blog/archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),

    # Example: /blog/archive/2019/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),

    # Example: /blog/archive/2019/nov/
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),

    # Example: /blog/archive/2019/nov/10/
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),

    # Example: /blog/archive/today/
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
    
    path('search/', views.SearchFormView.as_view(), name='search'),
>>>>>>> upstream/main
]