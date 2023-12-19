import django

from django.urls import include, re_path
from django.views import generic
from django.contrib import admin


urlpatterns = [
    re_path(r'^admin/', include(admin.site.urls)),
    re_path(r'^autocomplete/', include('autocomplete_light.urls')),
    re_path(r'^navigation/', include('navigation_autocomplete.urls')),
    re_path(r'^security_test/',
        include('autocomplete_light.example_apps.security_test.urls')),
    re_path(r'^non_admin_add_another/',
        include('autocomplete_light.example_apps.non_admin_add_another.urls')),
    re_path(r'^favicon.ico', generic.RedirectView.as_view(url='http://mozilla.org/favicon.ico')),
    re_path(r'^$', generic.TemplateView.as_view(template_name='index.html')),
    re_path(r'^bootstrap_modal/', include('bootstrap_modal.urls')),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
