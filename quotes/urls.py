from django.conf.urls import patterns, url

from quotes import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^quotes/newquote/$', views.add, name='add'),
	url(r'^quotes/gratitude/$', views.thanks, name='thanks'),
)