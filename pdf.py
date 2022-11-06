from pdf2image import convert_from_path


def get_pdf_data():
    PDF_file = "test.pdf"
    pages = convert_from_path(PDF_file, 500, poppler_path=r'D:\PycharmProjects\ocr\poppler-22.04.0\Library\bin')
    image_counter = 1
    for page in pages:
        filename = "page_" + str(image_counter) + ".png"
        page.save(filename, 'PNG')
        image_counter = image_counter + 1

get_pdf_data()

