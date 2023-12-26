from wordcloud import WordCloud
import numpy as np
from PIL import Image
import requests
from bs4 import BeautifulSoup

mask = Image.open("x.jpg")
maske_veri_2 = np.array(mask)

website_url = "https://www.kunstuni-linz.at/"

response = requests.get(website_url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
website_text = soup.get_text()

website_text = website_text.lower()
silinecek_ifadeler_2 = ["\"", "'",
                        "xml version='1.0' encoding='utf-8'?", "html", ""]
for ifade in silinecek_ifadeler_2:
    website_text = website_text.replace(ifade, "")

with open("[Icerik_Website].txt", "w", encoding="utf-8") as dosya:
    dosya.writelines(website_text)

mb = WordCloud(width=2000, height=2000,
               mask=maske_veri_2).generate(website_text)

mb.to_file("[Icerik_Gorsellestirme_Website].jpg")
