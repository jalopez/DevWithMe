from django import forms

class RelationshipForm(forms.Form):
    user = forms.CharField(max_length=255, label="Username")