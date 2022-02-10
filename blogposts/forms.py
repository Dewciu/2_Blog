from cgitb import text
from django import forms
from .models import Blogpost

class BlogpostForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    language = forms.ChoiceField(choices=Blogpost.Language.choices)


# class BlogpostForm(forms.ModelForm):
#     class Meta:
#         model = Blogpost
#         fields = [
#             'title',
#             'text',
#             'image',
#             'language'
#         ]