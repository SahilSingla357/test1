#python imports
#django imports
from django.db import models
from django.contrib.auth.models import User

#local imports
#inter app imports
#third party imports

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return (self.name)

class Post(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	created_on=models.DateTimeField(auto_now_add=True) 
	last_modified = models.DateTimeField(auto_now=True) 
	categories = models.ManyToManyField('Category', related_name='posts')
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=-1)

	def __str__(self):
		return (self.title)

class Comment(models.Model):
	author= models.ForeignKey(User, on_delete=models.CASCADE, default=-1) #models.CharField(max_length=100)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey('Post',on_delete=models.CASCADE)

	def __str__(self):
		return (self.body)

class Reply(models.Model):
    viewer = models.ForeignKey(User, on_delete=models.CASCADE, default=-1) #models.CharField(max_length=100)
    reply = models.TextField()
    comment = models.ForeignKey('comment',on_delete=models.CASCADE)

    def __str__(self):
        return (self.reply)

