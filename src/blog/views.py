from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .forms import EmailPostForm
from .models import Post


class PostListView(ListView):
    """Show All Post with Class-Based View"""
    queryset = Post.published.all()
    context_object_name = 'posts' # instead of object_list
    paginate_by = 3
    template_name = 'blog/post/list.html'


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


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent_by_email = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            print(cd)
            # https://docs.djangoproject.com/en/2.1/ref/request-response/#django.http.HttpRequest.build_absolute_uri
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{}({})recommends you reading {}'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {} \n\n{}\'s comments: {}'.format(post.title,
                                                                    post_url,
                                                                    cd['name'],
                                                                    cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent_by_email = True
    else:
        form = EmailPostForm()
    return render(request,
                  'blog/post/share.html',
                  {'post': post,
                   'form': form,
                   'sent': sent_by_email})
