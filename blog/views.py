from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.dates import YearArchiveView
from django.views.generic.dates import MonthArchiveView
from blog.models import Post
from django.utils import timezone

# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = 'posts'
    paginate_by = 1


class PostDV(DetailView):
    model=Post
    template_name="blog/post_detail.html"

class postArchiveView(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'
    template_name = "blog/post_archive.html"


class postYearArchiveView(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True
    template_name = "blog/post_archive_year.html"


class postMonthArchiveView(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = "blog/post_archive_month.html"