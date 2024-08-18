from django import forms
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _

from core.users.models import AgenteImobiliario


class AgenteImobiliarioChangeForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    foto = forms.ImageField(required=False)
    is_active = forms.BooleanField(required=False)
    telefone = forms.CharField(max_length=255, required=False)
    endereco = forms.CharField(max_length=255, required=False)

    class Meta:
        model = AgenteImobiliario
        fields = [
            "username",
            "password1",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "foto",
            "telefone",
            "endereco",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Se estamos editando (obj não é None)
        if self.instance and self.instance.user:
            user = self.instance.user
            self.fields["username"].initial = user.username
            self.fields["password1"].initial = user.password
            self.fields["email"].initial = user.email
            self.fields["first_name"].initial = user.first_name
            self.fields["last_name"].initial = user.last_name
            self.fields["is_active"].initial = user.is_active
            self.fields["foto"].initial = user.foto
            self.fields["telefone"].initial = user.telefone
            self.fields["endereco"].initial = user.endereco


class AgenteImobiliarioCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    is_active = forms.BooleanField(required=False)
    foto = forms.ImageField(required=False)
    telefone = forms.CharField(max_length=255, required=False)
    endereco = forms.CharField(max_length=255, required=False)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error("password2", error)

    class Meta:
        model = AgenteImobiliario
        fields = [
            "username",
            "password1",
            "password2",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "foto",
            "telefone",
            "endereco",
        ]
