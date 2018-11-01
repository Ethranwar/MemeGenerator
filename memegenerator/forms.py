from django import forms

class SentenceForm(forms.Form):
    original_sentence=forms.CharField(max_length=100,label='original sentence')
    changed_to_sentence=forms.CharField(max_length=100,label='changed to sentence')