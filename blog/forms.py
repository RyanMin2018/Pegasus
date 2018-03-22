# -*- coding: utf-8 -*-
from django import forms
from django.forms.models import inlineformset_factory
from .models import Blog, AttachedImage

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('category', 'title', 'text',)
        widgets = {
            'title':forms.TextInput(attrs={'placeholder':'제목이 필요해요'}),
        }
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''

BlogImageFormSet = inlineformset_factory(Blog, AttachedImage, fields=('img',), extra=2)
