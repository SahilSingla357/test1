#python imports
#django imports
from django import forms
#local imports
from .models import Category
#inter app imports
#third party imports


class commentForm(forms.Form):
	body = forms.CharField(widget=forms.Textarea(
		attrs={
		     "class":"form-control",
		     "placeholder":"comment here"
		})
	)

class replyForm(forms.Form):
    reply = forms.CharField(
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"enter your reply here"
            })
        )

class IndexForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"enter title here"}
        )
    )
    body = forms.CharField(
        widget=forms.Textarea(
        attrs={
             "class":"form-control",
             "placeholder":"enter body of Post"
        })
    )
    categories = forms.ModelChoiceField(
        queryset= Category.objects.all()
        )


    
