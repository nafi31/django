from django import forms
from .models import Title ,Item
class CreateList(forms.ModelForm):
    title = forms.CharField(label="Title",max_length=100,widget=forms.TextInput(
        attrs={
            "class":'form-control form-control-md',
        }
    ))
    content = forms.CharField(label="Content",max_length=10000,widget=forms.TextInput(
        attrs={
            "class":'form-control form-control-lg',
        }
    ))
  

    class Meta:
        model = Item
        fields = ('content',)
        models = Title
        fields = ('title',)