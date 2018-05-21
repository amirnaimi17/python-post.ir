from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatedFields, TranslatableModel


class StaticTypes(TranslatableModel):
    GROUP_TYPE = (
        ('ParcelType', _('ParcelType')),
        ('ParcelServiceType', _('ParcelServiceType')),
        ('ParcelDestType', _('ParcelDestType')),
        ('SendingMethod', _('SendingMethod')),
        ('ExtraTime', _('ExtraTime')),
        ('SPSReceivedTimeType', _('SPSReceivedTimeType')),
        ('SPSDestinationType', _('SPSDestinationType')),
        ('SPSParcelType', _('SPSParcelType')),
        ('InsuranceType', _('InsuranceType')),
    )

    group_type = models.CharField(_('group type'),choices=GROUP_TYPE, max_length=200)
    type = models.CharField(_('type'),max_length=200)
    value = models.PositiveIntegerField(_('value'))

    translations = TranslatedFields(
        lable=models.CharField(max_length=50, blank=True),
    )

    def save(self, *args, **skwargs):
        try:
            if not self.lable:
                self.lable = self.type
        except:
            self.lable = self.type

        super(StaticTypes, self).save(*args, **skwargs)

    def __str__(self):
        return self.lable
