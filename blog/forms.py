from django import forms

from django.contrib.auth.forms import User

from .models import PostModel, Comment, Profile


class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

    class Meta:
        model = PostModel
        fields = ('title', 'content')
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['title'].widget.attrs.update({ 
            'class': 'form-control', 
            }) 
        self.fields['content'].widget.attrs.update({ 
            'class': 'form-control', 
            }) 


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'content')
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['title'].widget.attrs.update({ 
            'class': 'form-control', 
            }) 
        self.fields['content'].widget.attrs.update({ 
            'class': 'form-control', 
            }) 


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'Add comment here....'}))

    class Meta:
        model = Comment
        fields = ('content',)
        def __init__(self, *args, **kwargs): 
            super().__init__(*args, **kwargs) 
            self.fields['content'].widget.attrs.update({ 
                'class': 'form-control', 
                }) 

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email']

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['username'].widget.attrs.update({ 
            'class': 'form-control', 
            'type':'text',
            }) 
        self.fields['first_name'].widget.attrs.update({ 
            'class': 'form-control', 
            'type':'text',
            }) 
        self.fields['last_name'].widget.attrs.update({ 
            'class': 'form-control', 
            'type':'text',
            }) 
        self.fields['email'].widget.attrs.update({ 
            'class': 'form-control', 
            'type':'email',
            }) 


""" class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['image'].widget.attrs.update({ 
            'class': 'form-control', 
            })  """
        