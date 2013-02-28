from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'quotes.views.index'),
	url(r'^newquote/$', 'quotes.views.add'),
	url(r'^gratitude/$', 'quotes.views.thanks'),
	url(r'^quotes/randquo/$', 'quotes.views.random_quote'),
    url(r'^admin/', include(admin.site.urls)),
)
