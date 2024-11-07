import pytesseract
from PIL import Image
import os


path = 'C:/Users/gtikd/Desktop/image_to_text/'
length = len(os.listdir(path))
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

for i in range(length):
    name = os.listdir(path)[i]
    image = Image.open(path+name)
    result = pytesseract.image_to_string(image, lang='kor')
    text_file_path = f'C:/Users/gtikd/Desktop/{os.path.splitext(name)[0]}.txt'
    with open(text_file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(result)
