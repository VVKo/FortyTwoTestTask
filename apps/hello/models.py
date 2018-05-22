from django.db import models


class Person(models.Model):
    """ Profile Model """

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="First name")

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Last name")

    birthday = models.DateField(
        blank=False,
        verbose_name="Birthday",
        null=True)

    email = models.EmailField()

    jabber = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Jabber")

    skype = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Skype")

    bio = models.TextField(
        blank=True,
        verbose_name="About me")

    contacts = models.TextField(
        blank=True,
        verbose_name="Additional contacts")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
