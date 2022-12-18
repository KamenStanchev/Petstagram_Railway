# import form as form
from django import forms
# from django.forms import fields

from main_app.models import Profile, Pet, PetPhoto


class DateInput(forms.DateInput):
    input_type = 'date'


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter pet name',
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'date_of_birth': DateInput(
                attrs={
                    'class': 'form-control',
                    'min': '1920-01-01',
                }),
        }


class EditPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter pet name',
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'date_of_birth': DateInput(
                attrs={
                    'class': 'form-control',
                    'min': '1920-01-01',
                }),
        }


class PhotoCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})



    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'tagged_pets')


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ('description', 'tagged_pets')
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'disabled': False,
                    'rows': 3
                }
            )
        }


class PhotoDeleteForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ('description', 'tagged_pets')
        widgets = {
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'readonly': 'readonly',
                }
            ),
            'tagged_pets': forms.Select(
                attrs={
                    'class': 'form-control',
                    'readonly': 'readonly',
                }),
        }


class DeletePetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class ': 'form-control',
                    'readonly': 'readonly',
                }
            ),
            'type': forms.Select(
                attrs={
                    'class ': 'form-control',
                    'readonly': 'readonly',
                }
            ),
            'date_of_birth': DateInput(
                attrs={
                    'class ': 'form-control',
                    'readonly': 'readonly',
                }),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter URL',
                }
            ),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ('account',)

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter URL',
                }
            ),
            'date_of_birth': DateInput(
                attrs={
                    'class': 'form-control',
                    'min': '1920-01-01',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter e-mail',
                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Write description about you',
                    'rows': 3,
                }
            ),
        }
