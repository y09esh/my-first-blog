from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.views.generic import ListView
#from django.utils import timezone
#from .forms import PostForm
"""def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 3) #3 posts in each page
    page = request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        #if page is not integer then deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        #If page is out of range then deliver last page of results
        posts=paginator.page(paginator.num_pages)            
    return render(request,
                  'blog/post/list.html',
                  {'page':page,'posts':posts})"""
class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name='blog/post/list.html'
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post':post})
"""def post_new(request):
    if request.method =="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html',{'form':form})
def post_edit(request, pk):
    post=get_object_or_404(Post, pk=pk)
    if request.method =="POST":
        form =PostForm(request.POST, instance = post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author= request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance = post)
    return render(request, 'blog/post_edit.html',{'form':form})
"""
