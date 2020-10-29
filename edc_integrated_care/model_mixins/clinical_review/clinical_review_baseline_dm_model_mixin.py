from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models
from edc_model.models import date_not_future


class ClinicalReviewBaselineDmModelMixin(models.Model):

    dm_test = models.CharField(
        verbose_name="Has the patient ever tested for Diabetes?",
        max_length=15,
        choices=YES_NO,
    )

    dm_test_ago = edc_models.DurationYMDField(
        verbose_name="If Yes, how long ago was the patient tested for Diabetes?",
        null=True,
        blank=True,
    )

    dm_test_estimated_datetime = models.DateTimeField(
        null=True, blank=True, help_text="calculated by the EDC using `dm_test_ago`",
    )

    dm_test_date = models.DateField(
        verbose_name="Date of patient's most recent Diabetes test?",
        validators=[date_not_future],
        null=True,
        blank=True,
    )

    dm_dx = models.CharField(
        verbose_name=mark_safe("Have you ever been diagnosed with Diabetes"),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text="If yes, complete form `Diabetes Initial Review`",
    )

    def save(self, *args, **kwargs):
        if self.dm_test_ago:
            self.dm_test_estimated_datetime = edc_models.duration_to_date(
                self.dm_test_ago, self.report_datetime
            )
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
