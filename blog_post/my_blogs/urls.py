from django.urls import path
from . import views
from myproject import settings
from django.conf.urls.static import static

urlpatterns=[
   
    path('',views.blogpage,name="blogpage"),
    path('get_blogs/<int:id>',views.get_blogs,name="get_blogs"),
    path('getlikes/<int:id>/<int:like_count>',views.getlikes,name="getlikes"),
    path('getdislikes/<int:id>/<int:dislike_count>',views.getdislikes,name="getdislikes"),
    path('logoutt/', views.bloglogout, name='logoutt'),
    path('savecomments/<int:userid>/<int:blogid>',views.savecomments,name="savecomments"),
    path('detailofblog/<int:id>',views.detailofblog,name="detailofblog"),
    path('delete_comments/<int:id>/<int:bid>',views.delete_comments,name="deletecomments"),
    path('show_comments/<int:bid>',views.show_comments,name="show_comments"),
    path('saveblogcontent/<int:user_id>',views.saveblogcontent,name="saveblogcontent"),
    path('approveblogs/',views.approveblogs,name='approveblogs'),
    path('approve_blog/<int:id>',views.approve_blog,name="approve_blog"),
    path('myposts/<int:id>',views.myposts,name="myposts"),
    path('editblogcontent/<int:id>/<int:userid1>',views.editblogcontent,name="editblogcontent"),
    path('myinactiveposts/<int:id>',views.myinactiveposts,name="myinactiveposts"),
     path('myunapprovedposts/<int:id>',views.myinactiveposts,name="myinactiveposts"),
    
    
    

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)