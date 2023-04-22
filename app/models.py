
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=10, validators=[MinLengthValidator(5)])#unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Ad(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, validators=[MinLengthValidator(20)])
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Selection(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

