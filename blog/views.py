from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , Http404
from .models import Article , Author , Readarticle , Mythought
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Count


# hello world model
def base(request):
    return render(request,'base.html')
def archive(request):
    author_info = Author.objects.all()
    tutorials = Article.objects.all().order_by('-created_at')
    return render(request,'archive.html',{'author_info':author_info, 'tutorials':tutorials})

def author_info(request):
    author_info = Author.objects.all()
    return render(request, 'author_info.html',{'author_info':author_info})

def readarticle(request, pk):
    author_info = Author.objects.all()
    tutorials = get_object_or_404(Article, pk=pk)
    tutorials.views += 1
    tutorials.save()
    return render(request, 'readarticle.html',{'tutorials':tutorials ,'author_info':author_info} )

def home(request):
    author_info = Author.objects.all()
    tutorials = Article.objects.all().order_by('-created_at')
    read_article = Readarticle.objects.all().order_by('-updated_at')
    return render(request, 'home.html',{'author_info':author_info , 'tutorials':tutorials, 'read_article':read_article})

def mythoughts(request):
    mythoughts = Mythought.objects.all()
    return render(request, 'mythoughts.html',{'mythoughts':mythoughts})
