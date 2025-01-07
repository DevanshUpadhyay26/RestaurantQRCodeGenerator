from django import forms


class QRForm(forms.Form):
    restaurant_form = forms.CharField(max_length=100, 
                                      label="Restaurant Name",
                                      widget=forms.TextInput(attrs={
                                          'class' : 'form-control',
                                          'placeholder': 'Enter restaurant name'
                                      }))
    url = forms.URLField(max_length=200, 
                         label="URL",
                         widget=forms.URLInput(attrs={
                             'class': 'form-control',
                             'placeholder':'Enter the URL of Menu'
                         }))
