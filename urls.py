from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from newsLetter.views import current_datetime, hours_ahead#, search

urlpatterns = patterns('',
                       (r'^time/$', current_datetime),
                       (r'^time/plus/(\d{1,2})/$', hours_ahead),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^search/$', "newsLetter.views.search"),
                       (r'^contact/$', "newsLetter.views.contact"),
                       (r'^signup/$', 'newsLetter.views.sign_up_view'),
                       )

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
