import PyPDF2
import glob
import os

pdf_files = ['2024 - Czerwiec 1.pdf', '2024 - Czerwiec 2.pdf']
base_dir = '/Users/kacperbogusz/Desktop/zse-inf04/arkusze'

for file in pdf_files:
    path = os.path.join(base_dir, file)
    txt_path = os.path.join(base_dir, 'extracted', file.replace('.pdf', '.txt'))
    
    with open(path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
            
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)
        
    print(f"Extracted {file}")
