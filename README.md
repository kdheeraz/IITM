steps to run wikipedia_extractor:
    pip install wikipedia (to install wikipedia API)
    pip install json (if json is not already installed)
    run the wiki_extractor.py



steps to run the pdf content extractor:
	install latest version of all the imports (pip install dependency_name if already exists do pip install --upgrade dependency_name
        download tesseract.exe and poppler
	download marathi language pack from https://github.com/tesseract-ocr/tessdata/ or for marathi (https://raw.githubusercontent.com/tesseract-ocr/tessdata/main/mar.traineddata)
        paste the file C:\\Program Files\\Tesseract-OCR\\tessdata (or wherever Tesseract OCR is installed).
        set TESSER_PATH(.exe) and POPPLER_PATH (til bin)

        run get_pdf.py
