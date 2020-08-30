from django import forms
#this form allows users to make suggestions for the website

class SuggestionsForm(forms.Form):
   data = forms.CharField(label = "Enter Here")
