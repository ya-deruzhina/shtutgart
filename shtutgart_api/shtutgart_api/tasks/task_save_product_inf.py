from shtutgart_api.celery import app
from apps.wb.models import *
from apps.wb.serializers import *
import requests

@app.task()
def save_product_inf_task (id_product):
    try:
        id_product = str(id_product)
        url_data = f'https://basket-14.wbbasket.ru/vol{id_product[:4]}/part{id_product[:6]}/{id_product}/info/ru/card.json'
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0',
            'Accept': '*/*',
            'Accept-Language': 'ru,en-US;q=0.7,en;q=0.3',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Origin': 'https://www.wildberries.ru',
            'Connection': 'keep-alive',
            'Referer': 'https://www.wildberries.ru/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
        }
        product_info = requests.get(url_data,headers=headers).json()
        
        name_product = product_info['imt_name']
        type_product = product_info['subj_name']
        root_type_product = product_info['subj_root_name']
        vendor_code = product_info['vendor_code']
        description = product_info['description']
        color = product_info['nm_colors_names']
        contents = product_info['contents']
        brand_name = product_info['selling']['brand_name']

        options = []
        inf_option = product_info['grouped_options']
        for option in inf_option:
            data = f'{option["group_name"]}: {option["options"][0]["name"]} - {option["options"][0]["value"]}'
            options.append(data)
        options = ", ".join(options)

        url_price = f'https://basket-14.wbbasket.ru/vol{id_product[:4]}/part{id_product[:6]}/{id_product}/info/price-history.json'
        data_price = requests.get(url_price,headers=headers).json()

        price_without_nds = float(str(data_price[-1]['price']['RUB'])[:-2])
        price = round(price_without_nds* 1.2328524)
        
        data = {
            "id":id_product,
            "name_product":name_product,
            "type_product":type_product,
            "root_type_product":root_type_product,
            "vendor_code":vendor_code,
            "description":description,
            "color":color,
            "contents":contents,
            "brand_name":brand_name,
            "options":options,
            "price_without_nds":price_without_nds,
            "price":price
        }

        serializer = CatalogSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    except:
        pass
    
    print(f'Done {id_product}')
