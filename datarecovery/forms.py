from django import forms
from .models import Device, FileType


class RecoveryForm(forms.Form):
    device = forms.ModelChoiceField(
        queryset=Device.objects.all(),
        label="Select Device",
        widget=forms.Select(attrs={'class': 'flex-1 py-2 px-4 w-full bg-slate-800 border border-white rounded-l-md'})
    )
    file_type = forms.ModelChoiceField(
        queryset=FileType.objects.all(),
        label="Select File Type",
        widget=forms.Select(attrs={'class': 'flex-1 py-2 px-4 w-full bg-slate-800 border border-white rounded-l-md'})
    )
