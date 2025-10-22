import mss
import mss.tools
from PIL import Image
import pytesseract
import time
pytesseract.pytesseract.tesseract_cmd = r'.\tesseract.exe'
import pyautogui
import glob
import os
files = glob.glob(r'.\Screenshots\*')
latest_file = max(files, key=os.path.getctime)
img = Image.open(latest_file)


# Extract text
extracted_text = pytesseract.image_to_string(img)
extracted_text = extracted_text.replace("\n", " ")
time.sleep(0.1)
print(extracted_text)
pyautogui.typewrite(extracted_text, interval=0.001)


