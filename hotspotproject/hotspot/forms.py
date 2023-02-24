from . models import Hotspot
from django import forms

class HotspotForm(forms.ModelForm):
    class Meta:
        model=Hotspot
        fields=['name','desc','image','date_added','year_added']