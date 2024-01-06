import PyPDF2

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
    page = reader.pages[0]
    page.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open('crooked_dummy.pdf', 'wb') as new_file:
        writer.write(new_file)



with open('twopage.pdf', 'rb') as file2:
    reader2 = PyPDF2.PdfReader(file2)
    print(len(reader2.pages))

