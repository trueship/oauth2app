def get_from_request_data(request, attr, default=None):
    return request.GET.get(attr, request.POST.get(attr, default))
