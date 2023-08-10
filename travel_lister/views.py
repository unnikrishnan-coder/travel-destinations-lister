from django.shortcuts import render
from django.http import Http404,FileResponse
from travel.scraper import scrapper
from travel import settings
import os

# Create your views here.
def index(req):
    return render(req,"travel_lister/index.html")

def generate(req):
    if(req.method == "POST"):
        data = req.POST['destination']
        if(data):
            result = scrapper(data)
            if(result["success"]):
                path_to_file = f"media/{settings.MEDIA_ROOT}/{result['filename']}"
                return render(req,"travel_lister/destinations.html",{"data":data,"filename":path_to_file})
            else:
                return render(req,"travel_lister/destinations.html",{"data":"error while getting destinations"})
        else:
            return Http404("bad request")
    else:
        return Http404("Invalid request")
    

def download_file(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    with open(file_path,"rb") as f:
        response = FileResponse(f)
        response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
        return response