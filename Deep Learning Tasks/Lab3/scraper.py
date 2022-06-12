import urllib.request,sys,time
from bs4 import BeautifulSoup
import requests
import pandas as pd

pagesToGet= 400

upperframe=[]  
filename="NEWS.csv"
f=open(filename,"w", encoding = 'utf-8')
headers="Link\n"
f.write(headers)
for page in range(1,pagesToGet+1):
    print('processing page :', page)
    url = 'https://www.politifact.com/factchecks/list/?page='+str(page)
    print(url)
    
    try:
        page=requests.get(url)                             
    
    except Exception as e:                               
        error_type, error_obj, error_info = sys.exc_info()    
        print ('ERROR FOR LINK:',url)                          
        print (error_type, 'Line:', error_info.tb_lineno)     
        continue                                         
    time.sleep(2)   
    soup=BeautifulSoup(page.text,'html.parser')
    frame=[]
    links=soup.find_all('li',attrs={'class':'o-listicle__item'})
    print(len(links))
    
    
    
    for j in links:
        Link = "https://www.politifact.com"
        Link += j.find("div",attrs={'class':'m-statement__quote'}).find('a')['href'].strip()
        f.write(Link+"\n")
    upperframe.extend(frame)
f.close()
data=pd.DataFrame(upperframe, columns=['Link'])
data.head()