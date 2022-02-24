from django import forms
from unicodedata import name
# from homestay.models.Destination import name

# from booking import forms


class AvailabilityForm(forms.Form):
    
    check_in = forms.DateField(required=True)
    check_out = forms.DateField(required=True)
    # amount = forms.IntegerField()
    # currency = forms.CharField(max_length=10)
    # receipt  = forms.CharField(max_length=10)





