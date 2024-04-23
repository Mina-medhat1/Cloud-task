import re
from collections import Counter
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords



try:
    with open("paragraphs.txt", "r") as file:
        text = file.read()
 
    stop_words = set(stopwords.words('english'))

    words = re.findall(r'\b\w+\b', text.lower())
    filtered_words = [word for word in words if word not in stop_words]

    word_counts = Counter(filtered_words)

    for word, count in word_counts.items():
        print(f"{word}: {count}")

except FileNotFoundError:
    print("Error: File 'random_paragraphs.txt' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
