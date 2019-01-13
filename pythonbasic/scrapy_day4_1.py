# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 20:01:53 2018

@author: jieyun
爬下skynews新闻某一篇的内容
"""

import bs4,requests

url='https://news.sky.com/story/harvey-weinstein-bragged-of-sex-with-jennifer-lawrence-lawsuit-alleges-11581435'

response=requests.get(url)
response.raise_for_status

with open(r'D:\Tutorial4MachineLearning\article.html','wb') as f:
    f.write(response.content)
    f.close()

file=open(r'D:\Tutorial4MachineLearning\article.html')  
fileSoup=bs4.BeautifulSoup(file.read())
elems=fileSoup.select('p')

fi=open(r'D:\Tutorial4MachineLearning\article.txt','w')  
for i in range(len(elems)):
    article=elems[i].getText()
    fi.write(article)
#将变量内容保存到本地
 
fi.close()
    
    