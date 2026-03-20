import requests 
import re
from bs4 import BeautifulSoup 
import matplotlib.pyplot as plt

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


textContent = soup.get_text()
textContent = textContent.lower()

words = re.findall(r'\b\w+\b', textContent)
wordFrequency = {}

for word in words:
    if(word in wordFrequency.keys()):
        wordFrequency[word] +=1
    else:
        wordFrequency[word] = 1

top5 = {}

findTopFive = wordFrequency.copy()

for i in range(5):
    maxKey = ''
    maxValue = 0
    for key, value in findTopFive.items():
        if(value>maxValue):
            maxValue = value
            maxKey = key
    top5[maxKey] = [maxValue]
    findTopFive.pop(maxKey)


keyWord = input("Enter what word you would like to know how many times it appears in the document: ")
try:
    print(f"{keyWord} appears {wordFrequency[keyWord]} times")
except:
    print("Word Not Found")



labels = ['Headings', 'Links', 'Paragraphs']
values = [count_h, count_a, count_p]

plt.bar(labels, values)

plt.title('Group 20') 
plt.ylabel('Count')
plt.xlabel('HTML Elements')

plt.show()


longest_paragraph = ''

for p in p_occurances:
    current = p.get_text().split()

    if len(p.get_text().split()) < 5:
        continue

    if len(current) > len(longest_paragraph):
        longest_paragraph = current



longest_paragraph_words = " ".join(longest_paragraph)
print(f"Longest paragraph: {longest_paragraph_words}")
print(f"This paragraph is {len(longest_paragraph)} word(s) long")