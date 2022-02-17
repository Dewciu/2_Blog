from multiprocessing import context
from turtle import title
from django.shortcuts import get_object_or_404, redirect, render
from .forms import BlogpostForm
from .models import Blogpost

# Create your views here.


def blogpost_create_view(request):
    form = BlogpostForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('/blog')
    
    context = {
        'form' : form
    }

    return render(request, 'blogpost_create.html', context)

def blogpost_list_view(request):
    blogposts = Blogpost.objects.all()
    context = {
        'blogposts':  blogposts
    }


    return render(request, 'blogpost_list.html', context)

def blogpost_detail_view(request, id):
    obj = get_object_or_404(Blogpost, id=id)

    context = {
        'object':   obj
    }
    return render(request, 'blogpost_detail.html', context)

def blogpost_delete_view(request, id):
    blogpost = Blogpost.objects.get(id=id)
    if request.method == 'POST':
        blogpost.delete()
        return redirect('/blog')
    context = {
        'blogpost' : blogpost
    }
    return render (request, 'blogpost_delete.html', context)