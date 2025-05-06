
from django import forms

class FolderUploadForm(forms.Form):
    folder = forms.FileField(
        label='Select Folder',
        widget=forms.ClearableFileInput(attrs={
            'directory': '',
            'webkitdirectory': '',
            'mozdirectory': '',
            'msdirectory': '',
        }),
        help_text='Select a folder containing ZIP files'
    )