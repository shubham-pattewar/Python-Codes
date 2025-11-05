# accounts/forms.py
from django import forms
import re
from django.core.exceptions import ValidationError

# Regex patterns
USERNAME_REGEX = r'^[A-Za-z0-9_]{4,20}$'
# ➤ allows letters, numbers, and underscore only, between 4 to 20 characters

PASSWORD_REGEX = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^\w\s]).{8,}$'
# ➤ must contain:
#    at least 1 uppercase, 1 lowercase, 1 digit, and 1 special character
#    minimum 8 characters long

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    # Validate username with regex
    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if not re.match(USERNAME_REGEX, username):
            raise ValidationError(
                "Username must be 4–20 characters (letters, digits, underscore only)."
            )
        return username

    # Validate password with regex
    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if not re.match(PASSWORD_REGEX, password):
            raise ValidationError(
                "Password must have 8+ chars, one uppercase, one lowercase, one digit, and one special symbol."
            )
        return password
