import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://x.com/meelonmuskusa'  # Replace with the actual URL you want to scrape

# Send an HTTP request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find and print all tweets on the page
# Note: Adjust the class names based on the actual HTML structure of the page
for tweet in soup.find_all('div', class_='tweet'):
    content = tweet.find('span', class_='content').get_text()
    timestamp = tweet.find('a', class_='timestamp').get_text()
    print(f'Tweet: {content}')
    print(f'Timestamp: {timestamp}')
    print('---')
