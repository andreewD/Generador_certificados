import pandas as pd
from PIL import Image,ImageDraw,ImageFont
data=pd.read_csv("data.csv",delimiter=";")
name_list=data["Nombres"].tolist()
for i in name_list:   
    im=Image.open(r"blanco.jpg")
    d=ImageDraw.Draw(im)
    location=(100,398)
    text_color=(0,137,209)
    font=ImageFont.truetype("arial.ttf",50)
    d.text(location,i,fill=text_color,font=font)
    im.save("certificate_" + i + ".pdf")