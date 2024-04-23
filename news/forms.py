from django.contrib.auth.models import User
from django import forms
from .models import News,Category,Comment


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']


class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=17)

class NewsForm(forms.ModelForm):

    class Meta:
        model=News
        fields=['title','text','tur','rasm']
    
    def __init__(self, *a, **b):
        super(NewsForm, self).__init__(*a, **b)
        self.fields['title'].widget.attrs.update({'class': 'input'})
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['tur'].widget.attrs.update({'class': 'form-control'})
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})



class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['izoh']




