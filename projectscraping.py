from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(executable_path=r"C:\Users\ADMIN\Desktop\chromedriver-win32")

products =[]
prices =[]

driver.get("http://www.flipkart.com/laptop/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")

content = driver.page_source

soup = BeautifulSoup(content, 'lxml')

for a in soup.findAll('a', href=True, attrs= {'class': '_31qSD5'}):
    name = a.find('div', attrs= {'class': '_3wU53n'})
    price = a.find('div', attrs= {'class': '_1vC4OE _2rQ-NK'})

    products.append(name)
    prices.append(price)

    print(name.text)
    print(price.text)

df = pd.DataFrame({'Product_name': products, 'Price': prices})

df.to_csv('products.csv', index=False, encoding='utf-8')


