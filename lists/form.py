from django import forms  
from .models import PostAd, DooSomething

PRIORITY = (
        ('Urgent' , 'Urgent'), 
        ('Hight' , 'Hight' ),
        ('Normal' , 'Normal' ),
    )

STATE = (
        ('Pending' , 'Pending'), 
        ('Done' , 'Done' ),
    )
class PostAdForm(forms.ModelForm):  
    error_css_class = 'error'

    priority = forms.ChoiceField(choices=PRIORITY, required=True )
    state = forms.ChoiceField(choices=STATE, required=True )

    class Meta:
        model = PostAd

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'What\'s the title of the task?'}),
            'date': forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
            'descripcion': forms.TextInput(attrs={'placeholder': 'Review the prototypes'}),
            'order': forms.TextInput(attrs={'placeholder': '1'}),
            #'priority': forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'})
        }