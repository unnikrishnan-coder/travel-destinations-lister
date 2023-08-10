from django.shortcuts import render
from django.http import HttpResponse,Http404
from .scraper import scrapper

# Create your views here.
def index(req):
    return render(req,"travel_lister/index.html")

def generate(req):
    if(req.method == "POST"):
        data = req.POST['destination']
        if(data):
            scrapper(data)
            return render(req,"travel_lister/destinations.html",{"data":data})
        else:
            return Http404("bad request")
    else:
        return Http404("Invalid request")