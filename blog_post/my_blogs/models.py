from django.db import models
from django.conf import settings

class Blog(models.Model):
   title = models.CharField(max_length=100, unique=True)
   body = models.TextField()
   posted = models.DateField(db_index=True, auto_now_add=True)
   category = models.ForeignKey('my_blogs.Category',on_delete=models.CASCADE)
   likes=models.IntegerField(blank=True,default=0)
   dislikes=models.IntegerField(blank=True,default=0)
   user_id=models.IntegerField(default=0,editable=False)
   Author=models.TextField(default='Admin')
   status=models.BooleanField(default=True)
   image=models.FileField(null=True, blank=True)
   blogrequest_id=models.IntegerField(default=0)
   # image = models.FilePathField(path='/images',blank=True)
#    blogs_comment= models.ForeignKey('my_blogs.Comments',on_delete=models.CASCADE)
   

   
   def __str__(self):
       return f"{self.title}"
class Category(models.Model):
   title = models.CharField(max_length=100, db_index=True)
   def __str__(self):
       return f"{self.title}"

class Comments(models.Model):
    comments=models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    blog=models.ForeignKey('my_blogs.Blog',on_delete=models.PROTECT)
    posted_date=models.DateField(db_index=True,auto_now_add=True)

    def __str__(self):
       return f"{self.user}--{self.comments}"
class Blogrequest(models.Model):
   firstname=models.TextField(blank=False)
   lastname=models.TextField(blank=False)
   emailid=models.EmailField(blank=False)
   mobileno=models.TextField(blank=True)
   blog_category=models.TextField(blank=False)
   blog_title=models.TextField(blank=False)
   blog_detail=models.TextField(blank=False)
   user_id=models.IntegerField()
   posted = models.DateField(db_index=True, auto_now_add=True)
   image=models.ImageField(null=True, blank=True)
   status=models.BooleanField(default=True)
   edit_status=models.BooleanField(default=True)

   



  

