from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    """Show All Post"""
    object_list = Post.published.all()
    # Instantiate the Paginator class with the number of objects we want to display on each page.
    paginator = Paginator(object_list, 3) # 3 posts in each page
    # indeicate the current page number
    current_page = request.GET.get('page')
    try:
        # Obtain the objects for the desired page
        posts = paginator.page(current_page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  'blog/post/list.html',
                  {'page': current_page, # page number
                   'posts': posts}) # retrieved object


def post_detail(request, year, month, day, post):
    """Show Desired Post"""
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
