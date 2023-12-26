import requests
import numpy as np
from PIL import Image
from bs4 import BeautifulSoup
from wordcloud import WordCloud


mask_image_location = input("Enter the mask image location: ")
mask = Image.open(f"{mask_image_location}")
mask_arr = np.array(mask)


website_url = input("Enter the URL: ")
html_content = requests.get(website_url).text
website_text = BeautifulSoup(html_content, 'html.parser').get_text()

delete_text = ["\"", "//", "'", "*", "\n", "\t",
               "xml version='1.0' encoding='utf-8'?", "html", ""]
for text in delete_text:
    website_text = website_text.replace(text, "")


mb = WordCloud(width=1000, height=1000, mask=mask_arr).generate(website_text)
save_file = input("Enter output file name: ")
mb.to_file(f"{save_file}.jpg")
