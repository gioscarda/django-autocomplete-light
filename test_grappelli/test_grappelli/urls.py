from django.urls import include, re_path
import autocomplete_light
autocomplete_light.autodiscover()
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^grappelli/', include('grappelli.urls')),
    re_path(r'autocomplete/', include('autocomplete_light.urls')),
]
# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'test_grappelli.views.home', name='home'),
#     # url(r'^test_grappelli/', include('test_grappelli.foo.urls')),
#
#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#
#     # Uncomment the next line to enable the admin:
#     url(r'^admin/', include(admin.site.urls)),
#     (r'^grappelli/', include('grappelli.urls')),
#     url(r'autocomplete/', include('autocomplete_light.urls')),
# )
