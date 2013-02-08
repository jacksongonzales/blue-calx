from django.contrib import admin
from quotes.models import Quote, QuoteForm


class QuoteAdmin(admin.ModelAdmin):
	list_display = ('text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']

admin.site.register(Quote, QuoteAdmin)
