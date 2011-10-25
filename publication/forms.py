from django import forms

class SnippetForm(forms.Form):
    title = forms.CharField(max_length=255, label="Title")
    text = forms.CharField(widget=forms.widgets.Textarea(), label="Code")
    is_public = forms.BooleanField("Public or only for your friends")
    tags = forms.CharField(max_length=255, label="Tags (separated by comma)", required=False)
    
    
class ReplyForm(forms.Form):
    title = forms.CharField(max_length=255, label="Title")
    text = forms.CharField(widget=forms.widgets.Textarea(), label="Text")