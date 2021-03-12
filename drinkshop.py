import requests as r
from bs4 import BeautifulSoup as bs
import pandas as pd


#ua = UserAgent()

#header = {'User-Agent':str(ua.chrome)}
baseurl = 'https://www.thedrinkshop.com/'
url = f'{baseurl}offers'
source =  r.get(url)
soup = bs(source.content)

products = soup.find_all('div',class_='col-xs-6 col-sm-6 col-md-4 col-lg-3')

pages = [1,2,3]


def add_products(prod):
    product_data = []
    for product in prod:
        try:
            ptitle = product.find('span',class_='title').text
            poffer = product.find('span',class_='offer').text
            psize = product.find('span',class_='size').text
            pprice = product.find('span',class_='price').text
            pstock = product.find('span',class_='stock in-stock').text.strip()
            ppiclink = product.find('img')['src']
            plink = product.find('a')['href']
            pdata = ptitle,poffer,psize,pprice,pstock,ppiclink,plink
            product_data.append(pdata)
    
        except:
            pass
    return product_data

df = pd.DataFrame(add_products(products))

print(df)


