from django.db import models


class City(models.Model):
    name = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Contact(models.Model):
    name = models.CharField(max_length=10)
    phone = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_auto_generated = models.BooleanField(default=False)

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="contacts",
        default=None,
        null=True,
        blank=False,
    )

    def __str__(self):
        return f'{self.name} , {self.phone}'

    __repr__ = __str__
