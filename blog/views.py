from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.

def Blog(request):
    message = 'Hello World'
    return HttpResponse(message)


def Words(request):
    return render(request, 'words.html', {'Python': 'Hello World'})


def post_list(request):
    posts = Post.objects.filter.order_by('published_date')
    return render(request, 'blog/words.html', {'posts': posts})
