from django.shortcuts import render
from myApp.models import Post
from myApp.models import Category

# Create your views here.

def home(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()[:5]

    data = {"post":posts,
            'cats':cats}
    return render(request,'index.html',data)

def post(request,url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()[:5]
    data = {"post":post,
            'cats':cats}
    return render(request,'post.html',data)

def category(request,url):
    cat = Category.objects.get(url=url)
    post = Post.objects.filter(cat=cat)
    return render(request,"category.html",{'cat':cat,'post':post})