from wordcloud import WordCloud
import numpy as np
from PIL import Image
import requests
from bs4 import BeautifulSoup

# Mask image
mask = Image.open("x.jpg")
maske_veri_2 = np.array(mask)

# Website URL
website_url = "https://www.kunstuni-linz.at/"

# Fetch content from the website
response = requests.get(website_url)
html_content = response.text

# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
website_text = soup.get_text()

# Preprocess the text
website_text = website_text.lower()
silinecek_ifadeler_2 = ["\"", "'",
                        "xml version='1.0' encoding='utf-8'?", "html", ""]
for ifade in silinecek_ifadeler_2:
    website_text = website_text.replace(ifade, "")

# Remove empty lines
website_text_lines = [line.strip()
                      for line in website_text.splitlines() if line.strip()]
website_text = '\n'.join(website_text_lines)

# Save the preprocessed text to a file
with open("[Icerik_Website].txt", "w", encoding="utf-8") as dosya:
    dosya.writelines(website_text)

# Generate word cloud
mb = WordCloud(width=2000, height=2000,
               mask=maske_veri_2).generate(website_text)

# Save the word cloud image
mb.to_file("[Icerik_Gorsellestirme_Website].jpg")
