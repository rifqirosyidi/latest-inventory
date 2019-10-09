from django import forms

from .models import Karyawan


class KaryawanCreateForm(forms.Form):
    nama = forms.CharField(max_length=100)
    nomor_handphone = forms.CharField(max_length=20)
    email = forms.EmailField()
    alamat = forms.CharField(widget=forms.Textarea)

    def clean_nomor_handphone(self):
        nomor_handphone = self.cleaned_data.get('nomor_handphone')

        def first_one(string):
            return string[:1]

        def first_three(string):
            return string[:3]

        if first_one(nomor_handphone) == '+':

            if first_three(nomor_handphone) == '+62':
                nomor_handphone = nomor_handphone
            else:
                raise forms.ValidationError("Please enter an indonesian format phone number '+62'")

        elif not nomor_handphone.isdigit():
            raise forms.ValidationError("Phone number must be numeric")

        elif not (12 <= len(nomor_handphone) <= 15):
            raise forms.ValidationError("Phone number length must be between 12 - 15")

        elif nomor_handphone[0] == '0':
            nomor_handphone = "+62%s" % nomor_handphone[0 + 1:]

        else:
            raise forms.ValidationError("Invalid phone numbers")

        return nomor_handphone

    def save(self):
        data = super().clean()
        user = Karyawan(
            nama=data['nama'],
            nomor_handphone=data['nomor_handphone'],
            email=data['email'],
            alamat=data['alamat']
        )

        user.save()


class KaryawanUpdateForm(forms.ModelForm):
    class Meta:
        model = Karyawan
        fields = '__all__'

    def clean_nomor_handphone(self):
        nomor_handphone = self.cleaned_data.get('nomor_handphone')

        def first_one(string):
            return string[:1]

        def first_three(string):
            return string[:3]

        if first_one(nomor_handphone) == '+':

            if first_three(nomor_handphone) == '+62':
                nomor_handphone = nomor_handphone
            else:
                raise forms.ValidationError("Please enter an indonesian format phone number '+62'")

        elif not nomor_handphone.isdigit():
            raise forms.ValidationError("Phone number must be numeric")

        elif not (12 <= len(nomor_handphone) <= 15):
            raise forms.ValidationError("Phone number length must be between 12 - 15")

        elif nomor_handphone[0] == '0':
            nomor_handphone = "+62%s" % nomor_handphone[0 + 1:]

        else:
            raise forms.ValidationError("Invalid phone numbers")

        return nomor_handphone

