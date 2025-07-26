import requests
from bs4 import BeautifulSoup

# Target website (simple example)
url = "https://www.w3schools.com/"

# Send a GET request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Extract all links
links = soup.find_all('a')

print("All links found on the URL homepage:\n")
for link in links:
    text = link.text.strip()
    href = link.get('href')
    if href and text:
        print(f"{text} --> {href}")
