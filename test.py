import datetime
from PIL import Image
import pyocr
import re

tools = pyocr.get_available_tools()
tool = tools[0]
now = datetime.datetime.now()
# print(tool)
# print(tool.get_name())

for z in range(1, 6):
    data = str(z)
    data = data.zfill(2)
    for i in [f"{data}.png"]:
        img = Image.open(f"images 2/{i}")
        txt = tool.image_to_string(
            img, lang="eng+jpn", builder=pyocr.builders.TextBuilder()
        )
        print(f"{now:%Y/%m/%d}の摂取カロリーは{txt}です")
        num = re.sub("[^0-9]", "", txt)
        print(num)
