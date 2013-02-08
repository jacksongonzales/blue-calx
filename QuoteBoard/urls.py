from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^quotes/$', 'quotes.views.index'),
	url(r'^quotes/newquote/$', 'quotes.views.add'),
	url(r'^quotes/gratitude/$', 'quotes.views.thanks'),
    url(r'^admin/', include(admin.site.urls)),
)