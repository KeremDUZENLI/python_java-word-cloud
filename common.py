import csv
from collections import Counter

csv_file_name = "results.csv"

website_words = {}
with open(csv_file_name, mode='r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)

    current_website = None
    website_word_list = []

    for row in reader:
        if 'WEB Adress' in row:
            if current_website:
                website_words[current_website] = website_word_list

            current_website = row[1]
            website_word_list = []

        elif len(row) == 2 and row[0] and row[1].isdigit():
            word, _ = row
            website_word_list.append(word)

    if current_website:
        website_words[current_website] = website_word_list

# Create a dictionary to store the websites where each word is common
common_words_tracker = {word: set()
                        for word in set.union(*map(set, website_words.values()))}

# Update the tracker based on common words
for website, words in website_words.items():
    for word in words:
        common_words_tracker[word].add(website)

# Filter words that are common between at least 2 websites
common_words_between_websites = {
    word: websites for word, websites in common_words_tracker.items() if len(websites) >= 2}

# Print the results
for word, websites in common_words_between_websites.items():
    print(
        f"Word '{word}' is common between {len(websites)} website(s): {', '.join(websites)}")
