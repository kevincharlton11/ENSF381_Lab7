import requests 

from bs4 import BeautifulSoup 

url = "https://en.wikipedia.org/wiki/University_of_Calgary" 
headers = { 
"User-Agent": "lab07-web-analyzer" 
} 
try: 
    response = requests.get(url, headers=headers) 
    response.raise_for_status()  # Ensures the request was successful 
    soup = BeautifulSoup(response.text, 'html.parser') 
    print(f"Successfully fetched content from {url}") 
except Exception as e: 
    print(f"Error fetching content: {e}")

#print(soup.prettify()) 

a_occurances = soup.find_all('a')
h_occurances = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
p_occurances = soup.find_all('p')

count_a = 0
count_h = 0
count_p = 0

for i in a_occurances:
    count_a = count_a + 1

for i in h_occurances:
    count_h = count_h + 1

for i in p_occurances:
    count_p = count_p + 1


print(count_p)