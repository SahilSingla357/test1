#python imports

#django imports
from django.conf import settings
from django.http import HttpResponse  #with render 
from django.views.generic import ListView, FormView, View, CreateView# or from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.shortcuts import render, redirect
#local imports

#inter app imports
from .models import Post, Comment ,Category, Reply
from .forms import commentForm, replyForm, IndexForm 



class IndexView(ListView):
    model = Post
    context_object_name = 'all_Post'
    template_name = 'index.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_on')

class IndexFormView(FormView):
    template_name='InputPost.html'
    form_class = IndexForm
    success_url = '/app/'

    def form_valid(self, form, **kwargs):
        
        r=Post(
            title=form.cleaned_data['title'],
            body=form.cleaned_data['body'],
            created_by =self.request.user
            )
        r.save()
        r.categories.add(form.cleaned_data['categories'])
        
        message='''
        Your post:-
        Title : '''+form.cleaned_data['title']+'''
        Body : '''+form.cleaned_data['body']+'''
        Has been successfully posted
        '''

        send_mail('confirmation of your post',message,settings.EMAIL_HOST_USER,['sahilsingla357@hotmail.com'], fail_silently=False)

        return redirect("/app/")


class CategoryOfPost(ListView):
    template_name = "category.html"
    model = Post

    def get_context_data(self,*args,**kwargs):
        category=self.kwargs.get('category')
        posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
        context={
        "category":category,
        "posts":posts,
        }
        return context

def details_of_post(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    # replies = Reply.objects.all()
    # form2=replyForm()
    form1=commentForm() 

    # if request.method =='POST' and 'htmlsubmitbutton2' in request.POST:
    #         form2 = replyForm(request.POST)
    #         if form2.is_valid() :
    #             r=Reply(
    #                 viewer=form2.cleaned_data["viewer"],
    #                 reply=form2.cleaned_data["reply"],
    #                 comment= request.POST.get('comment')
    #                 )
    #             r.save()

    if request.method =='POST' and 'htmlsubmitbutton1' in request.POST:
        form1 = commentForm(request.POST)
        if form1.is_valid():
            c= Comment(
                author=request.user, 
                body=form1.cleaned_data["body"],
                post=post
                 )
            c.save()
    
    context = {
        "post" : post,
        "comments" : comments,
        "form1":form1,
        # "form2":form2,
        # "replies":replies,
    }
    return render(request,"details.html",context)

class SignUpForBlog(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



