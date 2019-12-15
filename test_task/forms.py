from django import forms


class SampleForm(forms.Form):
    char = forms.CharField(label="Enter input", max_length=200,
    			widget=forms.TextInput(
            		attrs={
                		'style': 'border-color: orange;',
                		'placeholder': 'Enter characters'
            }
    	)
    )
    file = forms.FileField(label="Select File")