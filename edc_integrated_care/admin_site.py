from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = "Edc Morbidities"
    site_header = "Edc Morbidities"
    index_title = "Edc Morbidities"
    site_url = "/administration/"


edc_integrated_care_admin = AdminSite(name="edc_integrated_care_admin")
edc_integrated_care_admin.disable_action("delete_selected")
