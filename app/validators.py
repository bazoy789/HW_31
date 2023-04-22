import datetime

from django.core.exceptions import ValidationError


def stop_domain(value):
    domain = value.split("@")
    if domain[1] == "rambler.ru":
        raise ValidationError(
            f"registration with {domain[1]} prohibited"
        )


def check_is_publish(value):
    if value:
        raise ValidationError("not create published ads")


def check_birth_day(value):
    today = datetime.date.today()
    age = (today.year - value.year - 1) + ((value.month, value.day) >= (today.month, today.day))
    if age > 9:
        raise ValidationError(
            "younger then 9 years old"
        )
