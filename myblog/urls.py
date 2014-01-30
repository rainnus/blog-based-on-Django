from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from django.contrib import comments

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^blog/', include('myapp.urls')),
    #url(r'^show/', include('myapp.urls')),
)

urlpatterns += patterns('',
     (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),

)

urlpatterns += patterns('',

    (r'^comments/', include('django.contrib.comments.urls')),

)