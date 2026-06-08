from django import forms
from .models import Application
from courses.models import Course


class ApplicationForm(forms.ModelForm):
    full_name = forms.CharField(
        label="To'liq ism",
        widget=forms.TextInput(attrs={
            'placeholder': "Ism Familiya",
            'class': 'form-input',
        })
    )
    phone = forms.CharField(
        label="Telefon raqam",
        widget=forms.TextInput(attrs={
            'placeholder': "+998 90 123 45 67",
            'class': 'form-input',
        })
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.filter(is_active=True).order_by('order'),
        label="Kurs",
        empty_label="Kursni tanlang...",
        widget=forms.Select(attrs={
            'class': 'form-input',
        })
    )
    message = forms.CharField(
        label="Xabar (ixtiyoriy)",
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': "Savollaringiz yoki izohlaringiz...",
            'class': 'form-input',
            'rows': 4,
        })
    )

    class Meta:
        model = Application
        fields = ['full_name', 'phone', 'course', 'message']
