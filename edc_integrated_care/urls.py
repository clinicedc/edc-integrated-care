from django.urls import path
from django.views.generic.base import RedirectView

from .admin_site import edc_integrated_care_admin

app_name = "edc_integrated_care"

urlpatterns = [
    path("admin/", edc_integrated_care_admin.urls),
    path("", RedirectView.as_view(url="/edc_integrated_care/admin/"), name="home_url"),
]
