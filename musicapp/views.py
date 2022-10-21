
from django.http import httpresponse

# Create your views here.
def index(request):
    return httpresponse("My MusicApp")