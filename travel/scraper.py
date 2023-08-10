# import the required modules
import requests
from bs4 import BeautifulSoup as bs
from textwrap import wrap
import os
from fpdf import FPDF
import shutil

def scrapper(location):
    url = f"https://www.holidify.com/places/{location}/sightseeing-and-things-to-do.html"
    # parse the page
    try:
        page = requests.get(url)
        data = bs(page.text,'html.parser')

        # get the location and create the filename
        nav = data.find("nav",class_="navbar-secondary")
        location = nav.ul.li.a.get_text().lstrip().rstrip()
        filename = f"{location}.txt"
        pdf_filename = f"{location}.pdf"
        file_to_be_sent = pdf_filename

        # make the title
        page_title = data.title.string.rstrip().lstrip()
        if page_title.endswith("| Holidify"):
            title = page_title.split("|")[0]
        else:
            title = page_title

        # get the places
        h3s = data.find_all("h3",class_="card-heading")
        places = []
        for place in h3s:
            places.append(place.get_text().lstrip().rstrip())

        # writing the heading and places to txt file
        file = open(filename,"a")
        file.write(f"{title}\n")
        file.write("-"* len(title))
        file.write("\n")
        for place in places:
            file.write(f"{place} \n")
        file.close()

        # converting the txt file to pdf
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        f = open(filename, "r")
        for x in f:
            pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
        pdf.output(pdf_filename)
        f.close()
        # removing the txt file
        cwd = os.getcwd()
        file_path = os.path.join(cwd,filename)
        os.remove(file_path)

        # moving the pdf and opening it
        destination_dir = os.path.join(cwd,"media",pdf_filename)
        shutil.move(pdf_filename,destination_dir)
        return {"success":True,"filename":file_to_be_sent}
    except Exception as e:
        print(e)
        return {"success":False}