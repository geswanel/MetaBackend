from django import forms
from .models import Category

cat_choices = [(category.category_name, category.category_name) for category in Category.objects.all()]

class MenuItemForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200, widget=forms.widgets.Textarea)
    price = forms.FloatField()
    category = forms.ChoiceField(choices=cat_choices)