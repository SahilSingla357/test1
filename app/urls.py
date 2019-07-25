#python imports
from . import views

#django imports
from django.urls import path
from django.conf.urls import url
#local imports
from .views import *
#inter app imports

#third party imports


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', views.details_of_post, name='details'),
    path(r'(?P<category>[\w]+)/$', views.CategoryOfPost.as_view(), name='category'),
    #path('<int:pk1>/<int:pk2>', views., name='reply'),
    path('signup/', views.SignUpForBlog.as_view(), name='signup'),
    path('post/',views.IndexFormView.as_view(), name='enter-post')
]
