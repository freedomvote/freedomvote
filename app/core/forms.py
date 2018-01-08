from django import forms
from core.models import Politician, Party
from core.widgets import ImagePreviewFileInput
from django.utils.translation import gettext_lazy as _


class PoliticianForm(forms.ModelForm):
    class Meta:
        model = Politician
        exclude = ['unique_key', 'user']
        widgets = {
            'image': ImagePreviewFileInput()
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            if image.size > 5*1024*1024:
                raise forms.ValidationError('Image file too large ( > 5MB )')

        return image

    def clean_party_other(self):
        data = self.cleaned_data.get('party_other')

        if self.cleaned_data.get('party'):
            data = None

        return data

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(PoliticianForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.iteritems():
            if isinstance(field.widget, forms.TextInput) or isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    'class': 'form-control'
                })
            if field_name == 'party':
                field.choices = [('', '---------')]
                field.choices += [
                    (p.id, p.name)
                    for p
                    in Party.objects.order_by('name')
                ]

            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': 'form-control',
                    'rows': 2,
                })


class PartyPoliticianForm(forms.ModelForm):
    class Meta:
        model = Politician
        fields = ['first_name', 'last_name', 'email', 'state', 'is_member_of_parliament', 'user']

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(PartyPoliticianForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.iteritems():
            if isinstance(field.widget, forms.TextInput) or isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    'class': 'form-control'
                })


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label=_('First_name'), max_length=30)
    last_name = forms.CharField(label=_('Last_name'), max_length=30)
    email = forms.EmailField(label='Email')

    def clean_email(self):
        email = self.cleaned_data['email']

        try:
            Politician.objects.get(email=email)
        except Politician.DoesNotExist:
            return email
        raise forms.ValidationError(_('Email is already taken.'))
