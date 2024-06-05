from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Service(models.Model):
    title = models.CharField(_('service title'), max_length=255)
    description = models.TextField(_('service description'))

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')

    def __str__(self):
        return self.title
