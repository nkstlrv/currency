from django.utils.translation import gettext_lazy as _
from django.db import models


class RateCurrencyChoices(models.IntegerChoices):
    USD = 1, _("US Dollar")
    EUR = 2, _("Euro")
    UAH = 3, _("Hryvnia")
    PLN = 4, _("Polish Zloty")
    CHF = 5, _("Swiss Franc")
    BTC = 6, _("Bitcoin")


class RequestMethodChoices(models.IntegerChoices):
    GET = 0, _("GET")
    POST = 1, _("POST")