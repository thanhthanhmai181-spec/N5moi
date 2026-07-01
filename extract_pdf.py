import PyPDF2

try:
    reader = PyPDF2.PdfReader("c:\\Users\\ADMIN\\Desktop\\N5 T12-2021\\Script Nghe N5 T12-2021 Mark.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    with open("c:\\Users\\ADMIN\\Desktop\\N5 T12-2021\\script_extracted.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Extracted successfully.")
except Exception as e:
    print(f"Error: {e}")
