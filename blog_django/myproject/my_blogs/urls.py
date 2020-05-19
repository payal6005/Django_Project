from django.urls import path
from . import views

urlpatterns=[
   
    path('',views.blogpage,name="blogpage"),
    path('get_blogs/<int:id>',views.get_blogs,name="get_blogs"),
    path('getlikes/<int:id>/<int:l>',views.getlikes,name="getlikes"),
    path('getdislikes/<int:id>/<int:l>',views.getdislikes,name="getdislikes"),
    path('logout/', views.bloglogout, name='logout'),

]