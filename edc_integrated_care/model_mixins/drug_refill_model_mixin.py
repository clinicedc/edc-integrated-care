from django.conf import settings
from django.db import models
from edc_constants.choices import YES_NO

edc_integrated_care_listmodels = settings.EDC_MORBI_LISTMODELS


class DrugRefillModelMixin(models.Model):

    rx_other = models.CharField(
        verbose_name="If other, please specify ...",
        max_length=150,
        null=True,
        blank=True,
    )

    rx_modified = models.CharField(
        verbose_name=(
            "Was the patient’s prescription changed "
            "at this visit compared with their prescription "
            "at the previous visit?"
        ),
        max_length=25,
        choices=YES_NO,
    )

    modifications = models.ManyToManyField(
        edc_integrated_care_listmodels.get("rx_modifications"),
        verbose_name="Which changes occurred?",
        blank=True,
    )

    modifications_other = models.CharField(
        verbose_name="If other, please specify ...",
        max_length=150,
        null=True,
        blank=True,
    )

    modifications_reason = models.ManyToManyField(
        edc_integrated_care_listmodels.get("rx_modification_reasons"),
        verbose_name="Why did the patient’s previous prescription change?",
        blank=True,
    )

    modifications_reason_other = models.CharField(
        verbose_name="If other, please specify ...",
        max_length=150,
        null=True,
        blank=True,
    )

    return_in_days = models.IntegerField(
        verbose_name=(
            "In how many days has the patient been asked "
            "to return to clinic for a drug refill?"
        )
    )

    class Meta:
        abstract = True
