import pandas as pd
from newspaper import Article
import nltk
nltk.download('punkt')


urls = pd.read_csv('newsUrls.csv') 
urls = urls.values 

filename="output.csv"
output=open(filename,"w", encoding = 'utf-8')
headers="Link,FileName\n"
output.write(headers)

counter = 1
for url in urls:
    try:
        article = Article(url[0], language="en") # en for English 
        article.download() 
        article.parse() 
        article.nlp() 
        file1=open(str(counter) + ".txt", "w+")
        file1.write(article.text)
        file1.close()
        output.write(url[0] + ',' + str(counter) + ".txt" + '\n') 
        counter = counter + 1
    except:
        print("An exception occurred")
output.close()
    
