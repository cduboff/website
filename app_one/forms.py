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
    ingredients = forms.CharField(max_length=255)


class MealPlanForm(forms.Form):
    class Meta:
        widgets = {
            'text': forms.TextInput(attrs={
                'id': 'meal_text',
                'required': True,
                'placeholder': 'Day of the week'
            })
        }
    