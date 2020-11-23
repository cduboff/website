from django import forms

class PostForm(forms.Form):
    class Meta:
        widgets = {
            'text': forms.TextInput(attrs={
                'id': 'post-text', 
                'required': True, 
                'placeholder': 'Say something...'
            }),
        }
    ingredients = forms.CharField(label='Ingredients', max_length=255)