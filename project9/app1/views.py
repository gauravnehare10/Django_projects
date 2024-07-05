from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime
def display(request):
    dt = datetime.datetime.today()
    h = dt.hour
    if h <= 12:
        msg = '<h1>Good Morning</h1>'
    elif h <= 16:
        msg = '<h1>Good Evening</h1>'
    elif h <= 24:
        msg = '<h1>Good Night</h1>'

    output = f'''
    <html>
      <body>
        <h1>Current Date and Time is {dt}{msg}<h1>
        <a href="http://www.nareshit.com">NARESHIT</a>
      </body>
    </html>
    '''
    response = HttpResponse(output)
    return response
