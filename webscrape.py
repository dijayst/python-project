import requests as re
import json
from colorama import Fore,Back,Style
#from requests_html import HTMLSession
from bs4 import BeautifulSoup
 
#response = r.get(  , headers=headers)
 


def get_data(url):
  response=re.get(url,
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
       
  
  print(response)
  if response.status_code==200:
     print("The Status Code", response.status_code)
     print("The Response Text",response.text)
  else:
     print("failed to get data")
  soup=BeautifulSoup(response.text,"html.parser")
  print(soup)   
  print("-------------------prettify---------------------")
  print((soup.prettify))
  
  #Asos

  datae = []

  
  
  
  data=soup.find_all('article',{'class':'productTile_U0clN'})
  print(len(data))
  for items in data:
    img=items.find('div',{'class':'productMediaContainer_kmkXR'})
    
    price=items.find('p',{'class':'container_s8SSI'})
    print(img)
    print(price)
    
  data=soup.find_all('div',{'class':'B0CTMN9QMX'})
  for items in data:
    img=items.find('div',{'class':'productMediaContainer_kmkXR'})
    price=items.find('span',{'class':'a-price'})
    print(price)
    
    
    
  data=soup.find_all('section',{'class':'product-card'})
  print(len(data))
  for items in data:
    img=items.find('div',{'class':'productMediaContainer_kmkXR'})
    price=items.find('div',{'class':'product-card__goods-title-container'})
    print(price)
get_data("https://www.asos.com/women/shoes/heels/cat/?cid=6461")
get_data("https://www.jumia.com.ng/computer-accessories/")

print('------------------------------')

get_data('https://gadgetconnect.co.ke/computers/')
print('tyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
get_data('https://www.shein.com/RecommendSelection/Shoes-sc-017172966.html?adp=&categoryJump=true&ici=www_tab09navbar09&src_identifier=fc%3DShoes%60sc%3DShoes%60tc%3D0%60oc%3D0%60ps%3Dtab09navbar09%60jc%3DitemPicking_017172966&src_module=topcat&src_tab_page_id=page_home1717649548142')
print('----------------shein--------------')
