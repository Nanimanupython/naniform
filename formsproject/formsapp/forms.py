from django import forms


class EmployeeForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter ur first name'
            }
        )
    )
    second_name = forms.CharField(
        label='Second Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter ur second name'
            }
        )
    )
    salary = forms.CharField(
        label='Salary',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter ur salary'
            }
        )
    )
    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter ur address'
            }
        )
    )
