from PIL import Image
from pprint import pprint
import os
from tqdm import tqdm
import platform

if platform.system() == "Windows":
    os.system('cls')

path = os.path.join(os.path.expanduser('~'), 'Desktop')
folder = "image_to_pdf"
os.makedirs(os.path.join(path, folder), exist_ok=True)
print("바탕화면에 생성된 폴더에 사진을 넣으세요")
input("바탕화면의 폴더에 사진을 넣으셨다면 Enter를 누르세요...")
file_name=input('파일이름을 입력하세요 :')

file_list = os.listdir(os.path.join(path, folder))
img_list = []
# Use tqdm to track progress
for i in tqdm(file_list, desc="이미지를 PDF로 병합 중 입니다...."):
    try:
        img = Image.open(os.path.join(path, folder, i))
        img_1 = img.convert('RGB')
        img_list.append(img_1)
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {i}")
if img_list:
    img_list[0].save(os.path.join(path,file_name+'.pdf'),save_all=True, append_images=img_list[1:])
print("pdf 병합이 완료되었습니다. 바탕화면에서 생성된 pdf를 확인하세요.")