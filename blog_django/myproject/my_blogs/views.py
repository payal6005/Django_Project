from django.shortcuts import render,redirect
from django import template
from django.http import HttpResponse


from .models import Category,Blog
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout


def bloglogout(request):
    logout(request)
    return redirect("/")

def blogpage(request):
    obj=Category.objects.all()
    b = Blog.objects.all()[::-1]
    return render(request,"blog.html",{"categories":obj,"blog":b})

def get_blogs(request,id):
    
    obj=Category.objects.all()
    b = Blog.objects.filter(category__pk=id).select_related()
    return render(request,"blog.html",{"blog":b,"categories":obj})
@csrf_exempt
def getlikes(request,id,l):
   if   request.method == "POST":
        blog=Blog.objects.filter(id=id).update(likes=l+1)
        return
       
  
@csrf_exempt
def getdislikes(request,id,l):
   if   request.method == "POST":
        blog=Blog.objects.filter(id=id).update(dislikes=l+1)
        return render("/")
       
    

        
    
        



   


