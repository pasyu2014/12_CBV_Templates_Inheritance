from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Course

class CourseForm(ModelForm):
    """
    Форма для создания и редактирования курсов.
    """
    class Meta:
        model = Course
        fields = ['title', 'description', 'category', 'teachers', 'start_date', 'end_date', 'image']
        widgets = {
            'start_date': forms.DateInput(attrs={
                'placeholder': 'гггг-мм-дд (например, 2024-12-31)',
                'type': 'date',  # чтобы показать календарь в браузере
            }),
            'end_date': forms.DateInput(attrs={
                'placeholder': 'гггг-мм-дд (например, 2024-12-31)',
                'type': 'date',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if start_date and end_date and start_date > end_date:
            raise ValidationError("Дата начала должна быть раньше даты окончания.")
        return cleaned_data



"""
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Course

class CourseForm(ModelForm):
"""
    #Форма для создания и редактирования курсов.
"""
    class Meta:
        model = Course
        fields = ['title', 'description', 'category', 'teachers', 'start_date', 'end_date', 'image']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if start_date and end_date and start_date > end_date:
            raise ValidationError("Дата начала должна быть раньше даты окончания.")
        return cleaned_data
"""