from django import forms as f
from .models import D,DE,F,RE

class DF(f.ModelForm):
    class Meta:
        model=D
        fields=['t','d',]
class DEF(f.ModelForm):
    class Meta:
        model=DE
        fields=['t','c',]
class FF(DEF):
    f=f.FileField(widget=f.ClearableFileInput(attrs={'multiple': True}),required=False)
    class Meta(DEF.Meta):
        fields = DEF.Meta.fields + ['f',]