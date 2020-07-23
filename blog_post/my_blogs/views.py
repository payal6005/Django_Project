from django.shortcuts import render,redirect
from django import template
from django.http import HttpResponse,HttpResponseRedirect
from .models import Category,Blog,Comments,Blogrequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.contrib.auth.models import User
# from rest_framework.response import Response
import json
from django.core.files.storage import FileSystemStorage
from django.core.mail import BadHeaderError, send_mail
from myproject.settings import EMAIL_HOST_USER
from django.db.models import Q
import requests
import http.client





def bloglogout(request):
    logout(request)
    return redirect("/")

def blogpage(request):
    obj=Category.objects.all()
    b = Blog.objects.all()[::-1]
    
  
    for i in b:
       
       i.image=str(i.image).replace("my_blogs/","")
       c=Category.objects.get(id=i.category_id)
       i.category_id=c.title
     
    return render(request,"blog.html",{"categories":obj,"blog":b})

def get_blogs(request,id):
    
    obj=Category.objects.all()
    b = Blog.objects.filter(category__pk=id).select_related()[::-1]
    str1=""

    for i in b:
    
       i.image=str(i.image).replace("my_blogs/","")
       c=Category.objects.get(id=i.category_id)
       i.category_id=c.title
      
       
    return render(request,"blog.html",{"blog":b,"categories":obj})
@csrf_exempt
def getlikes(request,id,like_count):
   if   request.method == "POST":
        blog=Blog.objects.filter(id=id).update(likes=like_count)
        return
       
  
@csrf_exempt
def getdislikes(request,id,dislike_count):
   if   request.method == "POST":
        blog=Blog.objects.filter(id=id).update(dislikes=dislike_count)
        return 
@csrf_exempt
def savecomments(request,userid,blogid):
   ul = []
   info={}
   if request.method=="POST":
       
        c= Comments(user_id=userid,blog_id=blogid,comments=request.POST.get("blogcomment"))
        c.save()
        return redirect("/detailofblog/" + str(blogid)) 
      #   obj=Category.objects.all()
      #   b = Blog.objects.get(id=blogid)
      #   b.image=str(b.image).replace("my_blogs/","")
      #   c=Comments.objects.filter(blog_id=blogid).all()[::-1]
      #   for i in c:
        
      #      U=User.objects.get(id=i.user_id)
        
      #      info={
      #       "id": i.id,
      #       "blogid":blogid,
      #       "user":U.username,
      #       "comments":i.comments
            

      #       }
      #      ul.append(info)
         
     
          
     
          
      #   return render(request,'blog_detail.html',{"categories":obj,"blog":b,'alert_flag': True,"commentss":ul})
   elif request.method=="GET":
        obj=Category.objects.all()
        b = Blog.objects.get(id=blogid)
        b.image=str(b.image).replace("my_blogs/","")
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
        c=Category.objects.get(id=b.category_id)
        print(c)
        b.image=str(b.image).replace("my_blogs/","")
        ul = []
        info={}
        c=Comments.objects.filter(blog_id=id).all()
        for i in c:
        
           U=User.objects.get(id=i.user_id)
        
           info={
            "id": i.id,
            "blogid":id,
            "user":U.username,
            "comments":i.comments,
            "category":c
            

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
        
           
           
      # return render(request,'blog_detail.html',{"categories":obj,"blog":b,"commentss":ul})
   elif request.method=="GET":
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

        
         
   return HttpResponse(json.dumps(ul))
  
def show_comments(request,bid):
   ul = []
   info={}
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
def saveblogcontent(request,user_id):
   if request.method=="POST":
      print(request.POST.get("firstname"))
      if(request.POST.get("youtubelink")!=""):
         url = request.POST.get("youtubelink")
         url = url.replace("watch?v=", "embed/")
         blogcontent= Blogrequest(user_id=user_id,firstname=request.POST.get("firstname"),lastname=request.POST.get("lastname"),
         mobileno=request.POST.get("mobileno"),blog_category=request.POST.get("categoryname"),
         blog_title=request.POST.get("blogtitle"), blog_detail=request.POST.get("blogdetail"),
         emailid=request.POST.get("email"),image=url,edit_status=False)
         blogcontent.save()   
      else:
         myfile = request.FILES['imagefile']
         fs = FileSystemStorage()
     
         filename = fs.save(myfile.name, myfile)
     
         uploaded_file_url = fs.url(filename)
         blogcontent= Blogrequest(user_id=user_id,firstname=request.POST.get("firstname"),lastname=request.POST.get("lastname"),
         mobileno=request.POST.get("mobileno"),blog_category=request.POST.get("categoryname"),
         blog_title=request.POST.get("blogtitle"), blog_detail=request.POST.get("blogdetail"),
         emailid=request.POST.get("email"),image=myfile.name,edit_status=False)
         blogcontent.save()     
     
     
      return redirect("/")

def approveblogs(request):
   if request.method=='GET':
  
      obj=Category.objects.all()
      
      blog=Blogrequest.objects.filter(Q(status=1) | Q(edit_status=1)).all()[::-1]
     
      if blog != []:

         if(len(blog)>0):
        
          for i in blog:
            cat=Category.objects.get(id=i.blog_category)
            i.blog_category=cat
          
         else:
         
            cat=Category.objects.get(id=blog.blog_category)
            blog.blog_category=cat
            

          
     
   return render(request,"approveblog.html",{"categories":obj,"blog":blog})
def approve_blog(request,id):
      
      obj=Category.objects.all()

      blog1=Blogrequest.objects.filter(id=id)
      blog13=Blog.objects.filter(blogrequest_id=blog1[0].id)
      if(len(blog13)>0):

        blo2=Blog.objects.filter(blogrequest_id=blog1[0].id).update(title=blog1[0].blog_title,body=blog1[0].blog_detail,
        category_id=int(blog1[0].blog_category),status=1,Author=blog1[0].firstname + " "+blog1[0].lastname,image=blog1[0].image)
      else:

        blogcontent= Blog(title=blog1[0].blog_title,body=blog1[0].blog_detail,likes=0,dislikes=0,
        category_id=int(blog1[0].blog_category),status=1,user_id=blog1[0].user_id,Author=blog1[0].firstname + " "+blog1[0].lastname,image=blog1[0].image,
        blogrequest_id=blog1[0].id)
        blogcontent.save()
      Blogrequest.objects.filter(id=id).update(status=0,edit_status=0)
      blog=Blogrequest.objects.filter(status=1).all()[::-1]
     
      if blog :

       if(len(blog)>0):

         for i in blog:
            cat=Category.objects.get(id=int(i.blog_category))
            i.blog_category=cat
        
       elif(len(blog) == 0):
          cat=Category.objects.get(id=int(blog.blog_category))
          blog.blog_category=cat
         
       else:
         pass
      print(EMAIL_HOST_USER)
      msg="Dear "+str(blog1[0].firstname)+" "+str(blog1[0].lastname)+",\nYour Blog is Approved by Blogpost.Plz check below link.\nhttps://blogpost1837.herokuapp.com\nRegards,\nBlogPost"
      send_mail("BlogPost", msg , EMAIL_HOST_USER , [blog1[0].emailid],fail_silently = False)
      

          
      return redirect("/approveblogs",{"message":"success"})
def myposts(request,id):
   if request.method=='GET':
      cat=""
      obj=Category.objects.all()
      
      blog=Blogrequest.objects.filter(user_id=id,edit_status=0,status=0).all()[::-1]

      info={}
      ul=[]
    
      if blog != []:

         if(len(blog)>0):
          for i in blog:
            cat1=Category.objects.get(id=i.blog_category)

            info={
            "firstname": i.firstname,
            "lastname":i.lastname,
            "emailid":i.emailid,
            "mobileno":i.mobileno,
            "posted":i.posted,
            "image":i.image,
            "blog_title":i.blog_title,
            "blog_detail":i.blog_detail,
            "status":i.status,
            "category_name":cat1,
            "blog_category":i.blog_category,
            "id":i.id,
            "edit_status":i.edit_status
            
            

            }
           
            ul.append(info)  
         else:
          pass
   return render(request,"requestforeditblog.html",{"categories":obj,"blog":ul,"user_id":str(id)})
def myinactiveposts(request,id):
   if request.method=='GET':
      cat=""
      obj=Category.objects.all()
      
      blog=Blogrequest.objects.filter(Q(status=1) | Q(edit_status=1,user_id=id)).all()[::-1]

      info={}
      ul=[]
    
      if blog != []:

         if(len(blog)>0):
          for i in blog:
            cat1=Category.objects.get(id=i.blog_category)

            info={
            "firstname": i.firstname,
            "lastname":i.lastname,
            "emailid":i.emailid,
            "mobileno":i.mobileno,
            "posted":i.posted,
            "image":i.image,
            "blog_title":i.blog_title,
            "blog_detail":i.blog_detail,
            "status":i.status,
            "category_name":cat1,
            "blog_category":i.blog_category,
            "id":i.id,
            "edit_status":i.edit_status
            
            

            }
           
            ul.append(info)  
         else:
          pass
   return render(request,"requestforeditblog.html",{"categories":obj,"blog":ul,"user_id":str(id)})
   
def myunapprovedposts(request,id):
   if request.method=='GET':
      print(id)
      cat=""
      obj=Category.objects.all()
      
      blog=Blogrequest.objects.filter(user_id=id,edit_status=1).all()[::-1]
      
      info={}
      ul=[]
    
      if blog != []:

         if(len(blog)>0):
          for i in blog:
            cat1=Category.objects.get(id=i.blog_category)

            info={
            "firstname": i.firstname,
            "lastname":i.lastname,
            "emailid":i.emailid,
            "mobileno":i.mobileno,
            "posted":i.posted,
            "image":i.image,
            "blog_title":i.blog_title,
            "blog_detail":i.blog_detail,
            "status":i.status,
            "category_name":cat1,
            "blog_category":i.blog_category,
            "id":i.id,
            "edit_status":i.edit_status
            
            

            }
           
            ul.append(info)  
         else:
          pass
   print(ul)
   return render(request,"requestforeditblog.html",{"categories":obj,"blog":ul,"user_id":str(id)})
def editblogcontent(request,id,userid1):
   if request.method=="POST":
     
      if(request.POST.get("imagefile1")!=""):
         
         myfile = request.FILES['imagefile1']
         print(myfile)
         fs = FileSystemStorage()
     
         filename = fs.save(myfile.name, myfile)
     
         uploaded_file_url = fs.url(filename)
      
     
         Blogrequest.objects.filter(id=id).update(firstname=request.POST.get("firstname"),lastname=request.POST.get("lastname"),
         mobileno=request.POST.get("mobileno"),blog_category=request.POST.get("categoryname"),blog_title=request.POST.get("blogtitle"), blog_detail=request.POST.get("blogdetail"),
         emailid=request.POST.get("email"),image=myfile.name,edit_status=True)
      elif(request.POST.get("youtubelink")!=""):
         url = request.POST.get("youtubelink")
         url = url.replace("watch?v=", "embed/")
         Blogrequest.objects.filter(id=id).update(firstname=request.POST.get("firstname"),lastname=request.POST.get("lastname"),
         mobileno=request.POST.get("mobileno"),blog_category=request.POST.get("categoryname"),blog_title=request.POST.get("blogtitle"), blog_detail=request.POST.get("blogdetail"),
         emailid=request.POST.get("email"),edit_status=True,image=url)

      else:
         Blogrequest.objects.filter(id=id).update(firstname=request.POST.get("firstname"),lastname=request.POST.get("lastname"),
         mobileno=request.POST.get("mobileno"),blog_category=request.POST.get("categoryname"),blog_title=request.POST.get("blogtitle"), blog_detail=request.POST.get("blogdetail"),
         emailid=request.POST.get("email"),edit_status=True)

      
      
     
   return  redirect("/myposts/" + str(userid1))














        
    

        
    
        



   


