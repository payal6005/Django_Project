from django.db import models
from django.conf import settings

class Blog(models.Model):
   title = models.CharField(max_length=100, unique=True)
   body = models.TextField()
   posted = models.DateField(db_index=True, auto_now_add=True)
   category = models.ForeignKey('my_blogs.Category',on_delete=models.CASCADE)
   likes=models.IntegerField(blank=True)
   dislikes=models.IntegerField(blank=True)
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



  

