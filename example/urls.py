from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import redirect_to
from django.shortcuts import redirect

admin.autodiscover()

def zipfelchappe_payment(request):
    return redirect('zipfelchappe_paypal_payment')

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^$', redirect_to, {'url':'/projects/'}),
    url(r'^zipfelchappe/paypal/', include('zipfelchappe.paypal.urls')),
    url(r'^zipfelchappe/payment/$', zipfelchappe_payment,
        name='zipfelchappe_payment'),
    url(r'', include('feincms.urls')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^uploads/(.*)', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True,
            }),
    )
