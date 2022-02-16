from turtle import title
from django.shortcuts import get_object_or_404, render
from .forms import BlogpostForm
from .models import Blogpost

# Create your views here.


def blogpost_create_view(request):
    form = BlogpostForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        form=BlogpostForm()
    
    context = {
        'form' : form
    }

    return render(request, 'blogpost_create.html', context)

def blogpost_list_view(request):
    queryset = Blogpost.objects.all()
    context = {
        'object_list':  queryset
    }

    return render(request, 'blogpost_list.html', context)

def blogpost_detail_view(request, id):
    obj = get_object_or_404(Blogpost, id=id)
    context = {
        'object':   obj
    }
    return render(request, 'blogpost_detail.html', context)
