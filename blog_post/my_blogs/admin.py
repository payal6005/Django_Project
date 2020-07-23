from django.contrib import admin
from .models import Blog,Category,Comments

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('likes', 'dislikes','Author','blogrequest_id')
    
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Blog,BlogAdmin)



