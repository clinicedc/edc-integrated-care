from django.urls import path
from django.views.generic.base import RedirectView

from .admin_site import edc_morbi_admin

app_name = "edc_morbi"

urlpatterns = [
    path("admin/", edc_morbi_admin.urls),
    path("", RedirectView.as_view(url="/edc_morbi/admin/"), name="home_url"),
]
