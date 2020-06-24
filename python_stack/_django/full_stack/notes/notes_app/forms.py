from django import forms


class NoteForm(forms.Form):
    note = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class': 'form-control w-50'}))
