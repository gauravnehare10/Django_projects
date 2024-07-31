from datetime import datetime
from django.http import HttpResponse
class ExampleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('Before sending request to view')
        response = self.get_response(request)
        print('After sending request to view')
        return response
    
class TimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        dt = datetime.today()
        t = dt.time()
        m = dt.minute
        if t.hour > 8 and m > 50:
            response = HttpResponse('<h1>Currently this site not accepting any request</h1>')

        else:
            response = self.get_response(request)
        return response