from django.conf.urls import patterns, url

from quotes import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^newquote/$', views.add, name='add'),
	url(r'^gratitude/$', views.thanks, name='thanks'),
	url(r'^quotes/randquo/$', views.random_quote, name='random_quote'),
    url(r'^quotes/validatecomputer/$', 'ajax_validation.views.validate', {'form_class': QuoteForm}, 'quote_form_validate'),
)
