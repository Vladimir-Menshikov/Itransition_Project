from django import forms

class OrderByForm(forms.Form):
    FILTER_CHOICES = [
    ('name', 'Name'),
    ('-created', 'Date'),
    ]   
    order_by = forms.ChoiceField(widget=forms.Select(attrs=
                                       {'class': 'form-control',
                                        'onchange': 'orderByForm.submit();'
                                        }),
                          choices=FILTER_CHOICES)