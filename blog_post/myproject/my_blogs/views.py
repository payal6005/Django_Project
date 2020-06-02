from django.shortcuts import render,redirect
from django import template
from django.http import HttpResponse
from .models import Category,Blog,Comments
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.contrib.auth.models import User




def bloglogout(request):
    logout(request)
    return redirect("/")

def blogpage(request):
    obj=Category.objects.all()
    b = Blog.objects.all()[::-1]
    return render(request,"blog.html",{"categories":obj,"blog":b})

def get_blogs(request,id):
    
    obj=Category.objects.all()
    b = Blog.objects.filter(category__pk=id).select_related()[::-1]
    return render(request,"blog.html",{"blog":b,"categories":obj})
@csrf_exempt
def getlikes(request,id,like_count):
   if   request.method == "POST":
        blog=Blog.objects.filter(id=id).update(likes=like_count)
        return
       
  
@csrf_exempt
def getdislikes(request,id,l):
   if   request.method == "POST":
        blog=Blog.objects.filter(id=id).update(dislikes=l+1)
        return render("/")
@csrf_exempt
def savecomments(request,userid,blogid):
   ul = []
   info={}
   if request.method=="POST":
       
        c= Comments(user_id=userid,blog_id=blogid,comments=request.POST.get("blogcomment"))
        c.save()
        
        obj=Category.objects.all()
        b = Blog.objects.get(id=blogid)
        c=Comments.objects.filter(blog_id=blogid).all()[::-1]
        for i in c:
        
           U=User.objects.get(id=i.user_id)
        
           info={
            "id": i.id,
            "blogid":blogid,
            "user":U.username,
            "comments":i.comments
            

            }
           ul.append(info)
        return render(request,'blog_detail.html',{"categories":obj,"blog":b,'alert_flag': True,"commentss":ul})
   elif request.method=="GET":
        obj=Category.objects.all()
        b = Blog.objects.get(id=blogid)
        c=Comments.objects.filter(blog_id=blogid).all()[::-1]
        print(c)
        for i in c:
        
           U=User.objects.get(id=i.user_id)
        
           info={
            "id": i.id,
            "blogid":blogid,
            "user":U.username,
            "comments":i.comments
            

            }
           ul.append(info)
       
        return render(request,'blog_detail.html',{"categories":obj,"blog":b,"commentss":ul})
   else:
      pass

@csrf_exempt
def detailofblog(request,id):
  
        obj=Category.objects.all()
        b = Blog.objects.get(id=id)
        ul = []
        info={}
        c=Comments.objects.filter(blog_id=id).all()
        for i in c:
        
           U=User.objects.get(id=i.user_id)
        
           info={
            "id": i.id,
            "blogid":id,
            "user":U.username,
            "comments":i.comments
            

            }
           ul.append(info)

        
        
       
        return render(request,'blog_detail.html',{"categories":obj,"blog":b,"commentss":ul})
@csrf_exempt
def delete_comments(request,id,bid):
   ul = []
   info={}
   if request.method=="POST":

      a= Comments.objects.filter(id=id).delete()
      print(a)
      
      obj=Category.objects.all()
      b = Blog.objects.get(id=bid)
       
      c=Comments.objects.filter(blog_id=bid).all()
      print(c)
      for i in c:
        
           U=User.objects.get(id=i.user_id)
        
           info={
            "id": i.id,
            "blogid":bid,
            "user":U.username,
            "comments":i.comments
            

            }
           ul.append(info)
           print(ul)
        
           
           
      return render(request,'blog_detail.html',{"categories":obj,"blog":b,"commentss":ul})
   else:
      obj=Category.objects.all()
      b = Blog.objects.get(id=bid)
       
      c=Comments.objects.filter(blog_id=bid).all()
      for i in c:
        
           U=User.objects.get(id=i.user_id)
        
           info={
            "id": i.id,
            "blogid":bid,
            "user":U.username,
            "comments":i.comments
            

            }
           ul.append(info)

        
        
       
      return render(request,'blog_detail.html',{"categories":obj,"blog":b,"commentss":ul})







        
    

        
    
        



   


