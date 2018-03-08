'''importing urlopen function from request module inside 
urllib package as uReq,used for opening url links'''
from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup #importing beutifulsoup from bs4 as soup, used for scraping

my_url='https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphic+cards&N=-1&isNodeId=1'

uClient =uReq(my_url) #open up the connection,downloading web page
page_html=uClient.read() #store the data into a variable
uClient.close() #close the connection

page_soup=soup(page_html,"html.parser") #html parsing 

containers=page_soup.findAll("div",{"class":"item-container"}) #grabs each product

#open csv file and write data into it
filename="products_scrap.csv"
f=open(filename,"w")
headers="brand,product_name,shipping\n"
f.write(headers)

for container in containers: #loop through products
    brand=container.div.div.a.img["title"]  #find the brand name

    title_container=container.findAll("a",{"class":"item-title"}) #gives array of code with given class
    product_name=title_container[0].text #gives the product name

    shipping_container=container.findAll("li",{"class":"price-ship"}) #gives array of code with given class
    shipping=shipping_container[0].text.strip() #gives shipping type

    f.write(brand.replace(",","|")+","+product_name.replace(",","|")+","+shipping+"\n")
    
    print("brand: "+ brand)
    print("product_name: "+ product_name)
    print("Shipping: "+shipping)
f.close()
