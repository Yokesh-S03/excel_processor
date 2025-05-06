# from django import forms

# class FolderUploadForm(forms.Form):
#     folder_path = forms.CharField(
#         label='Folder Path',
#         widget=forms.TextInput(attrs={'type': 'text', 'id': 'folder-path'})
#     )
# processor/forms.py
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
