# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
import requests
from bs4 import BeautifulSoup

def article_read():
    url="http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
    data = requests.get(url)
    data.raise_for_status()
    soup=BeautifulSoup(data.text,"html.parser")
    article=soup.find_all("p")
    
    with open("article.txt",'a',encoding="utf-8") as file:
     for para in article:
        text=para.get_text(strip=True)
        if text:
            file.write(text+"/n/n")
            
    

if __name__ == "__main__":
    article_read()




    