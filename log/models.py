from django.db import models
from django.utils.translation import gettext_lazy as _


class Log(models.Model):

    action = models.CharField(verbose_name=_('Action'), max_length=63)
    app_label = models.CharField(verbose_name=_('APP label'), max_length=63)
    model_name = models.CharField(verbose_name=_('Model name'), max_length=63)
    data = models.TextField(verbose_name=_('Data'))
    created_at = models.DateTimeField(verbose_name=_('Created at'))