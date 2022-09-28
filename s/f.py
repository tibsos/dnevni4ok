from django import forms as f
from u.models import B

class BF(f.ModelForm):
    i=f.FileField(widget=f.ClearableFileInput(attrs={'style': 'display:none','id':'addFileButton'}))
    class Meta:
        model=B
        fields=['i',]

