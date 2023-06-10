from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

phone_re = "\\+?[1-9][0-9]{7,14}$"

validate_phone = RegexValidator(
    phone_re, _("Enter a valid phone number"),
)
