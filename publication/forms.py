from django import forms

class PublicationForm(forms.Form):
    title = forms.CharField(max_length=255, label="Title")
    text = forms.Textarea()
    is_public = forms.BooleanField("Public or only for your friends")
    tags = forms.CharField(max_length=255, label="Tags (separated by comma)")