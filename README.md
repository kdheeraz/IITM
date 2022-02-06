steps to run wikipedia_extractor:
    pip install wikipedia (to install wikipedia API)
    pip install json (if json is not already installed)
    run the wiki_extractor.py



steps to run the pdf content extractor:
        Note: Extracting data from whole pdf is taking very long, so current configuration fetches 1-10 pages/pdf, if required more remove first and last page condtion from

        pages = convert_from_path(PDF_file,poppler_path=POPPLER_PATH,dpi=200,first_page=1,last_page=10,fmt='jpg') (function: extract_text, file: get_pdf.py)

	install latest version of all the imports (pip install dependency_name if already exists do pip install --upgrade dependency_name
        download tesseract.exe and poppler
	download marathi language pack from https://github.com/tesseract-ocr/tessdata/ or for marathi (https://raw.githubusercontent.com/tesseract-ocr/tessdata/main/mar.traineddata)
        paste the file C:\\Program Files\\Tesseract-OCR\\tessdata (or wherever Tesseract OCR is installed).
        set TESSER_PATH(.exe) and POPPLER_PATH (til bin)

        run get_pdf.py
