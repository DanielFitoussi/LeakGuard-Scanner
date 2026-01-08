# simple test script
# trying to see if i can extract text from a pdf file
# this is just a first poc, not handling edge cases

import fitz #PyMuPDF

pdf_path = "poc/sample.pdf"

doc = fitz.open(pdf_path)

for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()
    print(f"---Page {page_num +1} ---")
    print(text)
    