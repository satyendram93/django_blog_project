from django.shortcuts import render, HttpResponse, redirect
from django.http import Http404
from django.contrib import messages
from . models import Blog
from .forms import BlogForm



def blog_home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'myblog/blog_home.html', context)

def blog_create_view(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog Created successfully.')
            return redirect('blog-list')
    else:
        form = BlogForm()
        
    context = {
        'form':form,   
    }
    return render(request, 'myblog/create_blog_form.html', context)


def blog_update_view(request, pk):
    try:
        ids = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=ids)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog Updated successfully.')
            return redirect('blog-list')
    else:
        form = BlogForm(instance=ids)
    context = {
        'form':form,   
    }
    return render(request, 'myblog/update_blog_form.html', context)

def blog_list_view(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'myblog/blog_list.html', context)

def blog_detail_view(request,pk):
    try:
        ids = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    context = {
        'blog': ids,
    }
    return render(request, 'myblog/blog_detail.html', context)
    

def blog_delete_view(request, pk):
    try:
        ids = Blog.objects.get(id=pk)
        ids.delete()
        messages.success(request, 'Blog deleted successfully.')
        return redirect('blog-list')
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    
