def dashboard(request) :
	form = FilterForm()
	sightings = []
	if request.POST :
		form = FilterForm(request.POST)
		if form.is_valid() :
			selectedplant = form.cleaned_data ['selectedplant']
			***sightings = Sighting.objects.filter(IMS_plant = selectedplant)
		else :
			sightings = Sighting.objects.all().order_by('date')
	else :
		sightings = Sighting.objects.all().order_by('date')
	context = {'sightings' : sightings, 'form' : form}
	return render_to_response('dashboard.html', context, context_instance = RequestContext(request))


def dashboard(request) :
	form = FilterForm()
	sightings = []
	if request.POST :
		form = FilterForm(request.POST)
		if form.is_valid() :
			selectedplant = form.cleaned_data ['selectedplant']
			***if selectedplant == None :
				***sightings = Sighting.objects.all().order_by('date')
			***else :
				sightings = Sighting.objects.filter(IMS_plant = selectedplant)
		else :
			sightings = Sighting.objects.all().order_by('date')
	else :
		sightings = Sighting.objects.all().order_by('date')
	context = {'sightings' : sightings, 'form' : form}
	return render_to_response('dashboard.html', context, context_instance = RequestContext(request))

