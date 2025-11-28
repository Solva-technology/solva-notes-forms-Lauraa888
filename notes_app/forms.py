from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["content", "status", "category", "author"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 4, "cols": 50}),
        }