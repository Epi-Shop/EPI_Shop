from django import forms
from .models import Epis, Carrinhos

class EpiForm(forms.ModelForm):
    class Meta:
        model = Epis
        fields = '__all__'  # Ou liste os campos que você quer no formulário

class AddToCartForm(forms.ModelForm):
    quantidade = forms.IntegerField(min_value=1, initial=1)
    epi = forms.ModelChoiceField(queryset=Epis.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Carrinhos
        fields = ['quantidade', 'epi']