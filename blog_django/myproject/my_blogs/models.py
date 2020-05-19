from django.db import models

class Blog(models.Model):
   title = models.CharField(max_length=100, unique=True)
   body = models.TextField()
   posted = models.DateField(db_index=True, auto_now_add=True)
   category = models.ForeignKey('my_blogs.Category',on_delete=models.CASCADE)
   likes=models.IntegerField(blank=True)
   dislikes=models.IntegerField(blank=True)
   comments=models.TextField(blank=True)

   
   def __str__(self):
       return f"{self.title}"
class Category(models.Model):
   title = models.CharField(max_length=100, db_index=True)
   def __str__(self):
       return f"{self.title}"

  

