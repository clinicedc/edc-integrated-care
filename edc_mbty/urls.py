from django.urls import path
from django.views.generic.base import RedirectView

from .admin_site import edc_mbty_admin

app_name = "edc_mbty"

urlpatterns = [
    path("admin/", edc_mbty_admin.urls),
    path("", RedirectView.as_view(url="/edc_mbty/admin/"), name="home_url"),
]
