from .models import Inventory
from django.contrib.auth.models import User


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'

        widgets = {
        	'opening_time': forms.TimeInput(attrs={'type':'time'}),
        	'closing_time': forms.TimeInput(attrs={'type':'time'}),
        }