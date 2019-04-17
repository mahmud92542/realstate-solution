from django.shortcuts import render
from listings.models import *
from realtors.models import *
from listings.choices import *


def about(request):
	#get all realtors
	realtors = Realtor.objects.order_by('-hire_date')

	#get MVP

	mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

	context = {
		'realtors': realtors,
		'mvp_realtors': mvp_realtors
	}

	return render (request,'pages/about.html',context)

def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
	context = {

		'listings': listings,
		'state_choices' : state_choices,
		'bedroom_choices' : bedroom_choices,
		'price_choices'	: price_choices

	}
	return render (request, 'pages/index.html',context)

