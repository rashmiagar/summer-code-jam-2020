from django import forms

from .models import Comment, Webpage, Template

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['title', 'content']

class WebpageForm(forms.ModelForm):

    class Meta:
        model = Webpage
        fields = ['name', 'thumbnail', 'template_used', 'user_title', 'user_text_1', 'user_text_2',
            'user_text_3', 'user_text_4', 'user_image_1', 'user_image_2', 'user_image_3',
            'user_image_4']

class TemplateForm(forms.ModelForm):

    class Meta:
        model = Template
        fields = ['name', 'style_sheet']