from django.db import models


class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birth = models.DateField()
    height = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

