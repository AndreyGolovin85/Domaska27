from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=8, decimal_places=6)
    lng = models.DecimalField(max_digits=8, decimal_places=6)

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


class UserRoles:
    USER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    choices = (
        (USER, "Пользователь"),
        (ADMIN, "Админ"),
        (MODERATOR, "Модератор")
    )


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(choices=UserRoles.choices, default="member", max_length=12)
    age = models.PositiveSmallIntegerField()
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователя"

    def __str__(self):
        return f"Пользователь: {self.first_name} {self.last_name}"
