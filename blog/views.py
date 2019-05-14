from django.shortcuts import render

# Create your views here.
from blog import models

def index(request):
    blog_index = models.Article.objects.all().order_by('-id')
    context = {
        'blog_index':blog_index,
    }
    return render(request, 'index.html',context)