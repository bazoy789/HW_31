from django.contrib.auth.models import AbstractUser

from django.db import models

from app.validators import check_birth_day, stop_domain


class Location(models.Model):
    name = models.CharField(max_length=200)
    lat = models.DecimalField(decimal_places=6, max_digits=8, null=True, blank=True)
    lng = models.DecimalField(decimal_places=6, max_digits=8, null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class User(AbstractUser):

    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLE = [(MEMBER, "Пользователь"), (MODERATOR, "Модератор"), (ADMIN, "Администратор")]

    role = models.CharField(max_length=10, choices=ROLE, default=MEMBER)
    age = models.PositiveSmallIntegerField(null=True)
    location = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[check_birth_day], null=True)
    email = models.CharField(max_length=50, validators=[stop_domain])#unique=True

    def save(self, *args, **kwargs):
        self.set_password(raw_password=self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]
