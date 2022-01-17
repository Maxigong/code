from django import forms


class UploadFileForm(forms.Form):
    img = forms.CharField(max_length=50)