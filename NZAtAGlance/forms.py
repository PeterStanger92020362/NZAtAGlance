from typing import ForwardRef
from django import forms
from django.core.validators import validate_email

class ChangeAgent(forms.ModelForm):

    def validate(self, value):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super().validate(value)
        for email in value:
            validate_email(email)

