from cgitb import text
from django import forms
from .widgets import DatePicker
from .models import Blogpost

class BlogpostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = [
            'title',
            'text',
            'image',
            'language',
            'date_of_publication'
        ]
        widgets = {
            'title'                 : forms.TextInput(
                                        attrs={
                                            'class'         : 'new-class-name one',
                                            'rows'          : 1,
                                            'cols'          : 50,
                                            'placeholder'   : 'Your Title'

                                            }
                                        ),
            'text'                  : forms.Textarea(
                                        attrs={
                                            'class' : 'new-class-name two',
                                            'rows'  : 20,
                                            'cols'  : 120,
                                            'placeholder'   : 'Please, write something interesting! :)'
                                        }
                                      ),
            'date_of_publication'   : DatePicker()
         }