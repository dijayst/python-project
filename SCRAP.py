import requests
import json
from bs4 import BeautifulSoup

def get_data(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    
    print(response)
    if response.status_code == 200:
        print("The Status Code:", response.status_code)
        print("The Response Text:", response.text[:200])  # Print first 200 chars for brevity
    else:
        print("Failed to get data")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
    print("-------------------prettify---------------------")
    print(soup.prettify()[:200])  # Print first 200 chars for brevity
    
    data = []

    # Example for ASOS
    product_tiles = soup.find_all('article', {'class': 'productTile_U0clN'})
    print("Number of ASOS products found:", len(product_tiles))
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
    
    # Save data to JSON
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

get_data("https://www.asos.com/women/shoes/heels/cat/?cid=6461")
get_data("https://www.jumia.com.ng/computer-accessories/")
print('------------------------------')
get_data('https://gadgetconnect.co.ke/computers/')
print('tyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
get_data('https://www.shein.com/RecommendSelection/Shoes-sc-017172966.html?adp=&categoryJump=true&ici=www_tab09navbar09&src_identifier=fc%3DShoes%60sc%3DShoes%60tc%3D0%60oc%3D0%60ps%3Dtab09navbar09%60jc%3DitemPicking_017172966&src_module=topcat&src_tab_page_id=page_home1717649548142')
print('----------------shein--------------')
