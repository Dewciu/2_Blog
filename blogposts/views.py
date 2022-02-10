from django.shortcuts import render
from .forms import BlogpostForm
from .models import Blogpost

# Create your views here.

def blogpost_create_view(request):
    form = BlogpostForm(request.POST or None)

    if form.is_valid():
        form.save()
        form=BlogpostForm()
    
    context = {
        'form' : form
    }

    return render(request, 'blogpost_create.html', context)

