from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models
from edc_model.models import date_not_future


class ClinicalReviewBaselineHtnModelMixin(models.Model):

    htn_test = models.CharField(
        verbose_name="Has the patient ever tested for Hypertension?",
        max_length=15,
        choices=YES_NO,
    )

    htn_test_ago = edc_models.DurationYMDField(
        verbose_name="If Yes, how long ago was the patient tested for Hypertension?",
        null=True,
        blank=True,
    )

    htn_test_estimated_datetime = models.DateTimeField(
        null=True, blank=True, help_text="calculated by the EDC using `htn_test_ago`",
    )

    htn_test_date = models.DateField(
        verbose_name="Date of patient's most recent Hypertension test?",
        validators=[date_not_future],
        null=True,
        blank=True,
    )

    htn_dx = models.CharField(
        verbose_name=mark_safe("Has the patient ever been diagnosed with Hypertension"),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text="If yes, complete form `Hypertension Initial Review`",
    )

    def save(self, *args, **kwargs):
        if self.htn_test_ago:
            self.htn_test_estimated_datetime = edc_models.duration_to_date(
                self.htn_test_ago, self.report_datetime
            )
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
