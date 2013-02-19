import datetime
from django.utils import timezone
from django.db import models
from django.forms import ModelForm, Textarea


class Quote(models.Model):
	text = models.TextField()
	who_said_it = models.CharField(max_length=128)
	pub_date = models.DateTimeField('date published', default=datetime.datetime.now)
	
#  	def __unicode__(self):
# 		return self.text
        
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		was_published_recently.admin_order_field = 'pub_date'
		was_published_recently.boolean = True
		was_published_recently.short_description = 'Published recently?'
		

class QuoteForm(ModelForm):	
	class Meta:
		model = Quote
		exclude = ('pub_date',)
		widgets = {
            'text': Textarea(attrs={'cols': 8, 'rows': 3}),
        }
