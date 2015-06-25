from django.conf.urls import include, url
from django.contrib import admin
from pythonmid.core.mediafiles import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^', include('pythonmid.apps.security.urls', namespace='security')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
]
