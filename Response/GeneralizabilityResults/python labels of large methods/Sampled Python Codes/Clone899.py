def queryset(self, request, queryset) :
	origin_GET = request.GET.copy()
	fake_GET = QueryDict(mutable = True)
	fake_GET.update(self.used_parameters)
	request.GET = fake_GET
	all_params = {}
	for spec in self.get_filters(request, self.used_parameters) :
		if spec and spec.has_output() :
			all_params.update(spec.used_parameters)
	try :
		query_params = [Q((key, value)) for key, value in all_params.items()]
		queryset = queryset.filter(reduce(operator.or_, query_params))
	except TypeError as e :
		pass
	request.GET = origin_GET
	return queryset


def queryset(self, request, queryset) :
	filters = request.GET.copy()
	try :
		search_field_value = filters.pop('q') [0]
		query_params = [Q((key, search_field_value)) for key in self.search_field]
		try :
			queryset = queryset.filter(reduce(operator.or_, query_params))
		except FieldError :
			pass
	except KeyError :
		pass
	try :
		query_params = [Q((key, value)) for key, value in filters.dict().items()]
		queryset = queryset.filter(reduce(operator.or_, query_params))
	except TypeError :
		pass
	return queryset

