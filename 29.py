# n this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single word.
import random
import requests
from bs4 import BeautifulSoup
print("hello")
url="https://norvig.com/ngrams/sowpods.txt"
request=requests.get(url)
soup=BeautifulSoup('request.text','html.parser')
words=soup.find('pre')

print("hello")
