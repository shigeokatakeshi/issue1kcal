from database import Kcal
from PIL import Image
import pyocr
import re

tools = pyocr.get_available_tools()
tool = tools[0]

# 01pngのみlayout8で読込
img = Image.open("images 2/01.png")
builder = pyocr.builders.TextBuilder(tesseract_layout=8)
txt = tool.image_to_string(img, lang="jpn", builder=builder)
num = re.sub("[^0-9]", "", txt)
Kcal.create(kcal=num)

# 02png~05pngはlayout6で読込
for z in range(2, 6):
    data = str(z)
    data = data.zfill(2)
    for i in [f"{data}.png"]:
        img = Image.open(f"images 2/{i}")
        builder = pyocr.builders.TextBuilder(tesseract_layout=6)
        txt = tool.image_to_string(img, lang="jpn", builder=builder)
        num = re.sub("[^0-9]", "", txt)
        Kcal.create(kcal=num)
