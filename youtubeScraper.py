from selenium import webdriver
from bs4 import BeautifulSoup
import json


urls = [
    'https://www.youtube.com/c/Freecodecamp/',
    'https://www.youtube.com/c/DevEd/featured',
    'https://www.youtube.com/c/CleverProgrammer',
]

def main():
    driver = webdriver.Chrome()
    
    for url in urls:
        
        driver.get('{}/videos?view=0&sort=p&flow=grid'.format(url))
        content = driver.page_source.encode('utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        titles = soup.findAll('a', id="video-title")
        views = soup.findAll('span', class_="style-scope ytd-grid-video-renderer")
        video_urls = soup.findAll('a',id='video-title')   
        print("Channel: {}".format(url))
        i = 0   
        j = 0
        lst = []
        for title in titles:
            print("\n {} \t{} \t {} \thttps://www.youtube.com{}".format(title.text, views[i].text, views[i+1].text, video_urls[j].get('href')))
            i += 2
            j += 1
            
            dictionary = {"title":titles,
                           "views":views,
                           "video_urls": video_urls}
            
        
main()

