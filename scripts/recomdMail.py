#python imports
import os,sys,django, pytz

#local imports

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test1.settings")
ROOT_FOLDER = os.path.realpath(os.path.dirname(__file__))
ROOT_FOLDER = ROOT_FOLDER[:ROOT_FOLDER.rindex('/')]
if ROOT_FOLDER not in sys.path:
    sys.path.insert(1, ROOT_FOLDER + '/')
django.setup()

#inter app imports
from app.models import Post, Category
#django imports
from django.contrib.auth.models import User
from django.core.mail import send_mail

#third party imports
from datetime import datetime, timedelta

EMAIL_HOST_USER='sahilsingla357@gmail.com'

for user in User.objects.all():
    categories=[]
    for post in Post.objects.all():
        if post.created_by_id==user.id:
            for category in post.categories.all():
                categories.append(category.name)

    categories=list(dict.fromkeys(categories))
    
    message='''Here are some Post recommanded to you based on your last week post: \n'''
    index=1
    for post in Post.objects.all():
        for category in post.categories.all():
            if (post.created_by_id!=user.id) and (category.name in categories) and (post.last_modified>pytz.utc.localize(datetime.now()-timedelta(days=7))):
                message += str(index)+'''. Post Title:'''+post.title+'''\n   Post Body:'''+post.body+'''\n   Created By:'''+post.created_by.username+'''\n'''
                index=index+1

    # print(message)
    send_mail('recommendation',message,EMAIL_HOST_USER,[user.email], fail_silently=False)
