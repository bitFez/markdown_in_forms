from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # exclude = ('short_link',)
        fields = ['title','content']
        

'''class Meta:
        model = Link
        exclude = ('short_link',)
        fields = ['title','original_link', 'tags', 'notes']
        widgets = {
            'notes': widgets.TextInput(attrs={
            'class': "textarea", 
            'style': 'max-width: 300px;',
            'placeholder': 'Add any notes about your list'
        })}'''