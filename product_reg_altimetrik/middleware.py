import json
from django.contrib.auth import authenticate
from django.http import HttpResponse
from product_reg_altimetrik.response import Response


class AuthenticateUserMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, *args, **kwargs):
        user = authenticate(username="skd", password="skd")
        if user is not None:
            return self.get_response(*args, **kwargs)
        else:
            return HttpResponse(status=401)


class ResponseConverterMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, *args, **kwargs):
        response = self.get_response(*args, **kwargs)
        if isinstance(response, Response):
            response_data = response.data
            if response_data is not None:
                return HttpResponse(json.dumps(response_data),
                                    status=response.status_code,
                                    content_type="application/json")
            else:
                # no data just sending the status code
                return HttpResponse(status=response.status_code)

        return response
