import requests
import numpy as np
from PIL import Image
from bs4 import BeautifulSoup
from wordcloud import WordCloud

# Mask image
mask_image_location = input("Enter the mask image location: ")
mask = Image.open(f"{mask_image_location}")
mask_arr = np.array(mask)

# Website URL
website_url = input("Enter the URL: ")

# Fetch content from the website
html_content = requests.get(website_url).text

# Parse HTML content with BeautifulSoup
website_text = BeautifulSoup(html_content, 'html.parser').get_text()

# Preprocess the text
delete_text = ["\"", "//", "'", "*", "\n", "\t",
               "xml version='1.0' encoding='utf-8'?", "html", ""]
for text in delete_text:
    website_text = website_text.replace(text, "")

# Save the preprocessed text to a file
with open("content.txt", "w", encoding="utf-8") as file:
    file.writelines(website_text)

# Generate word cloud
mb = WordCloud(width=1000, height=1000, mask=mask_arr).generate(website_text)

# Save the word cloud image
save_file = input("Enter output file name: ")
mb.to_file(f"{save_file}.jpg")
