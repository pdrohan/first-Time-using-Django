from django import forms
from PIL import Image


class Digitform(forms.Form):
    image = forms.ImageField()

