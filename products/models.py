from django.db import models
from django.utils.translation import gettext_lazy as _

from filebrowser.fields import FileBrowseField

# Create your models here.


class Product(models.Model):

    class Category(models.TextChoices):
        ACTIVE = 'AC', _('Active')
        PASSIVE = 'PA', _('Passive')
        WIRELESS = 'WI', _('Wireless')
        CAMERA = 'CA', _('CCTV Camera')
        TOWER = 'TO', _('Tower')
        POWER = 'PO', _('Power')

    name = models.CharField(_('product name'), max_length=255)
    category = models.CharField(
        _('product category'), max_length=2, choices=Category.choices
    )
    description = models.TextField(_('product description'))
    image = FileBrowseField(
        _('product image'),
        max_length=2255,
        directory='products/',
        extensions=['.jpg', '.jpeg', '.png'],
    )

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.name
