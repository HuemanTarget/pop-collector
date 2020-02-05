from django.forms import ModelForm
from .models import Detail

class DetailForm(ModelForm):
  class Meta:
    model = Detail
    fields = ['date', 'item_number', 'brand']