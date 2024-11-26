import requests
import json
from bs4 import BeautifulSoup
from colorama import Fore,Back,Style,init
init(convert=True)

def get_asos_data(soup):
    data = []
    product_tiles = soup.find_all('article', {'class': 'productTile_U0clN'})
    print(Fore.BLUE+"Number of ASOS products found:", len(product_tiles))
    for item in product_tiles:
        img = item.find('div', {'class': 'productMediaContainer_kmkXR'}).img['src'] if item.find('div', {'class': 'productMediaContainer_kmkXR'}).img else None
        details = item.find('p', {'class': 'productDescription_sryaw'}).text if item.find('p', {'class': 'productDescription_sryaw'}) else None
        price = item.find('p', {'class': 'container_s8SSI'}).text if item.find('p', {'class': 'container_s8SSI'}) else None
        print(details, img, price)
        data.append({
            'img': img,
            'details': details,
            'price': price
        })
    return data

def get_jumia_data(soup):
    data = []
    product_tiles = soup.find_all('article', {'class': 'prd _fb col c-prd'})
    print(Fore.GREEN+"Number of Jumia products found:", len(product_tiles))
    
    for item in product_tiles:
        img = item.find('div', {'class': 'img-c'}).img['src'] if item.find('div', {'class': 'img-c'}).img else None
        details = item.find('h3', {'class': 'name'}).text if item.find('h3', {'class': 'name'}) else None
        price = item.find('div', {'class': 'prc'}).text if item.find('div', {'class': 'prc'}) else None
        print(img, price)
        data.append({
            'img': img,
            'details':details,
            'price': price
        })
    return data

def get_gadgetconnect_data(soup):
    data = []
    product_tiles = soup.find_all('section', {'class': 'product-card'})
    print(Fore.YELLOW+"Number of GadgetConnect products found:", len(product_tiles))
    for item in product_tiles:
        img = item.find('div', {'class': 'productMediaContainer_kmkXR'}).img['src'] if item.find('div', {'class': 'productMediaContainer_kmkXR'}).img else None
        price = item.find('div', {'class': 'product-card__goods-title-container'}).text if item.find('div', {'class': 'product-card__goods-title-container'}) else None
        print(img, price)
        data.append({
            'img': img,
            'price': price
        })
    return data

def get_shein_data(soup):
    data = []
    product_tiles = soup.find_all('div', {'class': 'waterfall-item'})
    print("Number of Shein products found:", len(product_tiles))
    for item in product_tiles:
        img = item.find('img', {'class': 'fsp-element product-card__main-img crop-image-container__img'})['src'] if item.find('img', {'class': 'fsp-element product-card__main-img crop-image-container__img'}) else None
        details = item.find('div', {'class': 'product-card__goods-title-container'}).text if item.find('div', {'class': 'product-card__goods-title-container'}) else None
        price = item.find('p', {'class': 'product-card__camel-case-price prices-info__sale-price prices-info__sale-price_promo'}).text if item.find('p', {'class': 'product-card__camel-case-price prices-info__sale-price prices-info__sale-price_promo'}) else None
        print(details, img, price)
        data.append({
            'img': img,
            'details': details,
            'price': price
        })
    return data

def get_data(url, parser_function):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    
    if response.status_code == 200:
        print(f"The Status Code for {url}: {response.status_code}")
    else:
        print(f"Failed to get data from {url}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    data = parser_function(soup)
    return data

asos_data = get_data("https://www.asos.com/women/shoes/heels/cat/?cid=6461", get_asos_data)
jumia_data = get_data("https://www.jumia.com.ng/computer-accessories/", get_jumia_data)
gadgetconnect_data = get_data('https://gadgetconnect.co.ke/computers/', get_gadgetconnect_data)
#shein_data = get_data('https://www.shein.com/RecommendSelection/Shoes-sc-017172966.html?adp=&categoryJump=true&ici=www_tab09navbar09&src_identifier=fc%3DShoes%60sc%3DShoes%60tc%3D0%60oc%3D0%60ps%3Dtab09navbar09%60jc%3DitemPicking_017172966&src_module=topcat&src_tab_page_id=page_home1717649548142', get_shein_data)
shein_data=get_data('https://m.shein.com/pdsearch/heels/?ici=s1%60EditSearch%60heels%60_fb%60d0%60PagePreSearch&search_source=1&source=search&src_identifier=st%3D2%60sc%3Dheels%60sr%3D0%60ps%3D0&src_module=search&src_tab_page_id=page_pre_search1718014552212',get_shein_data)
# Combine all data
all_data = {
    "asos": asos_data,
    "jumia": jumia_data,
    "gadgetconnect": gadgetconnect_data,
    "shein": shein_data
}

# Save combined data to JSON
with open('data.json', 'w') as f:
    json.dump(all_data, f, indent=4)

print('Data scraping complete. Data saved to data.json')
