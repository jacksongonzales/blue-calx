import random
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse # Look into this thing
from quotes.models import Quote, QuoteForm

def index(request):
	random_idx = random.randint(0, Quote.objects.count() - 1)
	random_obj = Quote.objects.all()[random_idx]
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