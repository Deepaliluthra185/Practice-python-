# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
import requests
from bs4 import BeautifulSoup #beautifulsoup helps in easy reading of html text

def main():
    url = "https://www.nytimes.com/"
    request=requests.get(url) #it will fetch the url
    check=request.raise_for_status() #if any error occurs it stops programming
    soup=BeautifulSoup(request.text,"html.parser")#reads python text cleanly
    titles=soup.find_all("h2")#it will find h2 in html and store it in titles
    
    for title in titles:
     text = title.get_text(strip=True)# it will fetch text inside it
     if text:
        print("-",text)#it will print text5 

if __name__ =="__main__":
    main()

    