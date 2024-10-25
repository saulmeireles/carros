from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')

        if value is None:
            raise forms.ValidationError('O valor do carro deve ser informado.')
        
        if value < 20000:
            raise forms.ValidationError('Valor mínimo do carro deve ser R$ 20.000,00')

        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')

        if factory_year is None:
            raise forms.ValidationError('O ano da fábrica deve ser informado.')

        if factory_year < 1975:
            raise forms.ValidationError('Não é possível cadastrar carros fabricados antes de 1975')

        return factory_year
