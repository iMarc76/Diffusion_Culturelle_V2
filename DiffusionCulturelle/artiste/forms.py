from django import forms
from .models import Artiste, Spectacle, Date, Lieu


class DateForm(forms.ModelForm):
    class Meta:
        model = Date
        fields = ['date']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder':'Date'})
        }


class ArtisteForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control ', 'placeholder': 'name@example.com', 'id': 'validationCustomUsername',
                   'aria-describedby': 'inputGroupPrepend'}
        )
    )

    class Meta:
        model = Artiste
        fields = '__all__'

        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'website': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Site Internet'})
        }

class SpectacleForm(forms.ModelForm):
    animation = forms.ChoiceField(
        choices=[(True, "Oui"), (False, "Non")],
        widget=forms.RadioSelect,
        initial=False,
        label="Animation ",

    )
    class Meta:
        model = Spectacle
        fields = '__all__'
        exclude = ['artiste', 'lieu', 'user']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du spectacle'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'public': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Public'}),
            'duree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Durée'})
        }

class LieuForm(forms.ModelForm):

    class Meta:
        model = Lieu
        fields = '__all__'
        widgets = {
            'nom_lieu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du lieu'}),
            'rue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rue'}),
            'num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro'}),
            'cp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code postal'}),
            'ville': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ville'})

        }










