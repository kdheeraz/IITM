import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import pandas as pd
import image
import pytesseract
import sys
from pdf2image import convert_from_path
import json


def extract_text(filename):
    PDF_file = filename

    TESSER_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    POPPLER_PATH = r"C:\Users\DreamCatcher\Desktop\poppler-22.01.0\Library\bin" #include bin

    pytesseract.pytesseract.tesseract_cmd = TESSER_PATH

    '''
    Part #1 : Converting PDF to images
    '''

    # Store all the pages of the PDF in a variable
    try:
        pages = convert_from_path(PDF_file,poppler_path=POPPLER_PATH,dpi=200,first_page=1,last_page=10,fmt='jpg')
    except:
        return "Invalid Pdf"
    print("converted to image")

    # Counter to store images of each page of PDF to image
    image_counter = 1

    #outfile = "out_text.txt"

    # Open the file in append mode so that
    # All contents of all images are added to the same file
    #f = open(outfile, "a", encoding="utf-8")

    # Iterate through all the pages stored above
    complete_text = ""
    for page in pages:

        filename = "page1"+".jpg"
            
            # Save the image of the page in system
        page.save(filename, 'JPEG')

        text = str(((pytesseract.image_to_string(filename,lang="mar"))))

        
        
        text = text.replace('-\n', '')

        
        
        if(text):
            print(text)
            # Finally, write the processed text to the file.
            #f.write(text)
            complete_text += text


            # Increment the counter to update filename
        image_counter = image_counter + 1

    '''
    Part #2 - Recognizing text from the images using OCR
    '''
            
    # Variable to get count of total number of pages
    filelimit = image_counter-1

    return complete_text[-300:]


csv_cont = pd.read_csv("task.csv")

urls = list(csv_cont["https://mpsctopper.com/wp-content/uploads/2022/01/12th-std-Political-Science-Book-in-Marathi.pdf"])

urls.insert(0,"https://mpsctopper.com/wp-content/uploads/2022/01/12th-std-Political-Science-Book-in-Marathi.pdf")

#print(urls)

json_data = []
content = ""

for url in urls:
    if ".pdf" in url:
        with open("pdffile.pdf", 'wb') as f:
            f.write(requests.get(url).content)
        content=extract_text("pdffile.pdf")
        json_data.append({"page-url":url,"pdf-url":url, "pdf-content":content})
        with open("pdf_extract.json", 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)


    
    else:
        response = requests.get(url)
        soup= BeautifulSoup(response.text, "html.parser")

        links =[]
        for link in soup.select("a[href$='.pdf']"):
            if urljoin(url,link['href']) not in links:
                        print("downloading pdf from ",urljoin(url,link['href']))
                        
                        with open("pdffile.pdf", 'wb') as f:
                            f.write(requests.get(urljoin(url,link['href'])).content)
                        content=extract_text("pdffile.pdf")
                        json_data.append({"page-url":url,"pdf-url":str(urljoin(url,link['href'])), "pdf-content":content})
                        with open("pdf_extract.json", 'w', encoding='utf-8') as f:
                            json.dump(json_data, f, ensure_ascii=False, indent=4)
                        links.append(urljoin(url,link['href']))    


                
                

        
        

















url = "https://archive.org/details/marathi_202111/page/n7/mode/2up?view=theater"

#If there is no such folder, the script will create one automatically

def fetch_pdfs(url):
    response = requests.get(url)
    soup= BeautifulSoup(response.text, "html.parser")

    links =[]
    for link in soup.select("a[href$='.pdf']"):
        if link not in links:
            links.append(urljoin(url,link['href']))
    #print("links",links)    
    
'''for link in soup.select("a[href$='.pdf']"):
    print(link)
    #Name the pdf files using the last portion of each link which are unique in this case
    filename = link['href'].split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)'''
