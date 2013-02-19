import random
from django.core import serializers
import json
from django.utils import simplejson
from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse # Look into this thing
from quotes.models import Quote, QuoteForm

def randomizer():
	random_idx = random.randint(0, Quote.objects.count() - 1)
	random_obj = Quote.objects.all()[random_idx]
	return random_obj

def index(request):
	random_obj = randomizer()
	return TemplateResponse(request, 'quotes/index.html', {
		'quote': random_obj,
	})
    
def add(request):
	if request.method == 'POST':
		form = QuoteForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/quotes/gratitude/')
	
	else:
		form = QuoteForm()
		
	return TemplateResponse(request, 'quotes/add.html', {
		'form': form,
		
	})
	
def thanks(request):
	 return TemplateResponse(request, 'quotes/thanks.html')
	 
def random_quote(request):
	#test if ajax request
	response = randomizer()
	jsondata = serializers.serialize("json", [response]) #why need square brackets?
# 	jsondata = simplejson.dumps(response.__dict__)
	print jsondata
	return HttpResponse(jsondata, mimetype='application/json') #is mimetype necessary?
	