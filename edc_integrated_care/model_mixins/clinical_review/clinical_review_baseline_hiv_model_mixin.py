from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models
from edc_model.models import date_not_future


class ClinicalReviewBaselineHivModelMixin(models.Model):

    hiv_test = models.CharField(
        verbose_name="Has the patient ever tested for HIV infection?",
        max_length=15,
        choices=YES_NO,
    )

    hiv_test_ago = edc_models.DurationYMDField(
        verbose_name="How long ago was the patient's most recent HIV test?",
        null=True,
        blank=True,
        help_text="If positive, most recent HIV(+) test",
    )

    hiv_test_estimated_datetime = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        help_text="calculated by the EDC using `hiv_test_ago`",
    )

    hiv_test_date = models.DateField(
        verbose_name="Date of patient's most recent HIV test?",
        validators=[date_not_future],
        null=True,
        blank=True,
    )

    hiv_dx = models.CharField(
        verbose_name=mark_safe(
            "Has the patient ever tested <U>positive</U> for HIV infection?"
        ),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text="If yes, complete form `HIV Initial Review`",
    )

    def save(self, *args, **kwargs):
        if self.hiv_test_ago:
            self.hiv_test_estimated_datetime = edc_models.duration_to_date(
                self.hiv_test_ago, self.report_datetime
            )
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
