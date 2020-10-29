from django.db import models


class ClinicalReviewModelMixin(models.Model):
    def get_best_hiv_test_date(self):
        return self.hiv_test_date or self.hiv_test_estimated_datetime

    def get_best_dm_test_date(self):
        self.dm_test_date or self.dm_test_estimated_datetime

    def get_best_htn_test_date(self):
        self.htn_test_date or self.htn_test_estimated_datetime

    @property
    def diagnoses(self):
        return dict(hiv=self.hiv_dx, htn=self.htn_dx, dm=self.dm_dx)

    @property
    def diagnoses_labels(self):
        return dict(hiv="HIV", htn="Hypertension", dm="Diabetes")

    class Meta:
        abstract = True
