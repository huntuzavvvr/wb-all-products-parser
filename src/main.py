import json
import requests
import pprint


url = 'https://static-basket-01.wb.ru/vol0/data/main-menu-ru-ru-v2.json'

response = requests.get(url).json()
with open("categories.json", 'w', encoding='utf-8') as f:
    json.dump(response, f, ensure_ascii=False, indent=4)
with open('categories.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
jon = json.dumps(data[0], ensure_ascii=False)

# 0 уровень
for i in data:
    category = i
    category_list = []

    if category.get("childs") is not None and category.get("name") not in "Региональные товарыВкусы России":
        # 1 уровень
        sub1_category_list = category.get("childs")
        for sub1_category in sub1_category_list:
            if sub1_category.get("childs") is not None:
                # 2 уровень
                sub2_category_list = sub1_category.get("childs")
                for sub2_category in sub2_category_list:
                    API = f"https://catalog.wb.ru/catalog/{sub2_category.get('shard')}/catalog?appType=1&{sub2_category.get('query')}&curr=rub&dest=-1257786&page=1&sort=popular&spp=0"
                    print(API, sub2_category.get("name"))

            else:
                API = f'https://catalog.wb.ru/catalog/{sub1_category.get("shard")}/catalog?appType=1&{sub1_category.get("query")}&curr=rub&dest=-1257786&page=1&sort=popular&spp=0'
                print(API, sub1_category.get("name"))
