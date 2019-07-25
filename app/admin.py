#python imports

#django imports
from django.contrib import admin
from django.conf.urls import url

#local imports
from .models import *

#inter app imports

#third party imports

# Register your models here.
class PostAdmin(admin.ModelAdmin):
 	pass

class CategoryAdmin(admin.ModelAdmin):
 	pass #?
'''
class CustomAdminSite(admin.AdminSite):
	def get_urls(self):
		urls = super(CustomAdminSite, 
self).get_urls()
		custom_urls = [
		url(r'de')]
'''

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(Reply)