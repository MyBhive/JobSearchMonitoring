from django import forms
from .models import JobOffer, Categories


class JobOfferForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = (
            'category_id',
            'user_id',
            'title',
            'company_name',
            'url',
            'salary',
            'comments',
            'status_id',
            'style_id',
            'type_id',
            'cv',
            'motiv_letter',
        )
        widgets = {
            'category_id': forms.Select(attrs={'class': 'form-control'}),
            'user_id': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'actual-user', 'type': 'hidden'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'job name...'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company...'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write your own comment here...'}),
            'status_id': forms.Select(choices='choice_list', attrs={'class': 'form-control'}),
            'style_id': forms.Select(attrs={'class': 'form-control'}),
            'type_id': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(JobOfferForm, self).__init__(*args, **kwargs)
        self.fields['category_id'].queryset = \
            Categories.objects.filter(user_id=user)
