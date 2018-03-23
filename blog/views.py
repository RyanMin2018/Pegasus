# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.http import HttpResponse#, JsonResponse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
#from django.contrib import messages
from .models import Blog, AttachedImage, Category, Comment
from .forms import BlogForm, BlogImageFormSet, CommentForm

# List Page
def blog_list(request):
    intPageSize = 10

    # category
    catid = request.GET.get('cat')
    catnm = ""
    list  = Blog.objects.select_related('category')
    if catid:
        catnm = get_object_or_404(Category, pk=catid).category_name
        list  = list.filter(category=catid)
    list = list.order_by('-published_date')

    # pagination
    paginator = Paginator(list, intPageSize)
    page      = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog_list.html', {
            'posts':posts,
            'totalcnt':paginator.count,
            'pagesize':intPageSize,
            'category':catid,
            'category_name':catnm
        }
    )

# Detail Page
def blog_detail(request, pk):
    post  = get_object_or_404(Blog.objects.select_related('category'), pk=pk)
    page  = request.GET.get('page')
    if not page:
        page = 1
    catid = request.GET.get('cat')
    files = AttachedImage.objects.filter(blogid=pk)
    return render(request, 'blog/blog_detail.html', {
            'post': post,
            'page':page,
            'files':files,
            'category':catid,
            'post_author':post.author,
        }
    )

# Upload Image. Using InLineFormSet_Factory.
def uploadImageFile(request, bid):
    blogid = Blog.objects.get(pk=bid)
    if request.method == "POST":
        imgForm = BlogImageFormSet(request.POST, request.FILES, instance=blogid)
        if imgForm.is_valid():
            imgForm.save()

# Regist Page
def blog_new(request):
    if request.method == "POST" and request.user.is_authenticated:
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            uploadImageFile(request, post.pk)
            return redirect('blog:blog_detail', str(post.pk))
    else:
        if request.user.is_authenticated:
            form = BlogForm()
            ImageFormSet = BlogImageFormSet(form_kwargs={'label_suffix': ''})
            return render(request, 'blog/blog_form.html', {
                    'form':form,
                    'fileform':ImageFormSet,
                    'strPageTitle':'등록',
                    'post_author':request.user
                }
            )
        else:
            return render(request, 'registration/access_deny.html')

# Edit Page
def blog_edit(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST" and request.user.is_authenticated:
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            uploadImageFile(request, post.pk)
            return redirect('blog:blog_detail', str(post.pk))
    else:
        if request.user.is_authenticated and request.user == post.author:
            form = BlogForm(instance=post)
            blogid       = Blog.objects.get(pk=post.pk)
            ImageFormSet = BlogImageFormSet(instance=blogid,
                                            form_kwargs={'label_suffix': ''})
            return render(request, 'blog/blog_form.html', {
                    'form': form,
                    'fileform':ImageFormSet, 
                    'strPageTitle':'수정',
                    'post_author':post.author
                }
            )
        else:
            return render(request, 'registration/access_deny.html')

# Delete Post
def blog_delete(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.user.is_authenticated and request.user == post.author:
        post.delete()
        return redirect('blog:blog_list')
    else:
        return render(request, 'registration/access_deny.html')


# Get category name and that's count of articles.
# it's called by main/templates/main/layout.html
def blog_category_count(request):
    list = Blog.objects.select_related('category')
    list = list.values('category', 'category__category_name')
    list = list.annotate(count=Count('pk'))
    res = ''
    for c in list:
        res += '<li onclick="location.href=\''+resolve_url('blog:blog_list')
        res += '?cat='+str(c.get('category'))+'\'">'
        res += '<a href="'+resolve_url('blog:blog_list')
        res += '?cat='+str(c.get('category'))+'">'
        res += c.get('category__category_name')
        res += ' - ' + format(c.get('count'), ',')
        res += '</a>'
        res += '</li>'
    return HttpResponse(res)

# Comments List
def comment_list(request, pk):
    comments = Comment.objects.filter(blogid=pk)
    res = '['
    for c in comments:
        res += '{'
        res += '"author":"' + str(c.author) + '",'
        res += '"comment":"' + str(c.comment) + '",'
        res += '"dt":"' + str(c.created_date.strftime("%Y.%m.%d %H:%M:%S")) + '",'
        res += '"id":"' + str(c.id) + '"'
        res += '},'
    res = res.rstrip(',')
    res += ']'
    return HttpResponse(res)

# Add Comment
def comment_new(request, pk):
    blogid = Blog.objects.get(pk=pk)
    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.blogid = blogid
            post.save()
            return HttpResponse(str(post.pk))
    else:
        return render(request, 'registration/access_deny.html')

# Delete Comment
def comment_delete(request, pk, id):
    post = get_object_or_404(Comment, pk=id)
    if request.user.is_authenticated and request.user == post.author:
        post.delete()
        return HttpResponse(str(id))
    else:
        return render(request, 'registration/access_deny.html')