from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , Http404
from .models import Article , Author , Readarticle
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Count


# hello world model
def base(request):
    return render(request,'base.html')
def temp(request):
    author_info = Author.objects.all()
    tutorials = Article.objects.all().order_by('-created_at')
    read_article = Readarticle.objects.all().order_by('-updated_at')
 
    return render(request, 'temp.html',{'author_info':author_info , 'tutorials':tutorials, 'read_article':read_article})

def readarticle(request, pk):
    tutorials = get_object_or_404(Article, pk=pk)
    tutorials.views += 1
    tutorials.save()
    return render(request, 'readarticle.html',{'tutorials':tutorials} )


def home1(request):
    try:
        tutorials = Article.objects.all()
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'home1.html',{'tutorials':tutorials})

def simple_upload(request):

        author_info = Author.objects.all()
        return render(request, 'home1.html',{'author_info':author_info})
