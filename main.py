import requests
from bs4 import BeautifulSoup

products_to_track = [
    {
        "product_url": "https://www.flipkart.com/redmi-9-activ-metallic-purple-64-gb/p/itm329ae4068c8e8?pid=MOBG7F5HVHHNVXGK&lid=LSTMOBG7F5HVHHNVXGKINZYEE&marketplace=FLIPKART&q=mobiles&store=tyy%2F4io&srno=s_1_3&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&fm=organic&iid=a3c9d909-3780-4319-b248-45d70d01fd06.MOBG7F5HVHHNVXGK.SEARCH&ppt=hp&ppn=homepage&ssid=zetz0hn8io0000001667797457989&qH=eb4af0bf07c16429",
        "name": "Samsung M31",
        "target_price": 16000
    },
    {
        "product_url": "https://www.flipkart.com/motorola-e40-pink-clay-64-gb/p/itm5d6f2871d1bbf?pid=MOBG2EMW2ZUR4BFG&lid=LSTMOBG2EMW2ZUR4BFGEC0C0J&marketplace=FLIPKART&q=mobiles&store=tyy%2F4io&srno=s_1_5&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&fm=organic&iid=951140fc-e684-418f-9133-49e53fbcfc7e.MOBG2EMW2ZUR4BFG.SEARCH&ppt=hp&ppn=homepage&ssid=5s6ga8t86o0000001667803224657&qH=eb4af0bf07c16429",
        "name": "Samsung M21 6GB 128RAM",
        "target_price":16000
    },
    {
        "product_url": "https://www.flipkart.com/infinix-hot-12-play-champagne-gold-64-gb/p/itmd9c1091d0a662?pid=MOBGE2KYE4DA7ZPF&lid=LSTMOBGE2KYE4DA7ZPFIXECD0&marketplace=FLIPKART&q=mobiles&store=tyy%2F4io&srno=s_1_6&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&fm=organic&iid=951140fc-e684-418f-9133-49e53fbcfc7e.MOBGE2KYE4DA7ZPF.SEARCH&ppt=hp&ppn=homepage&ssid=5s6ga8t86o0000001667803224657&qH=eb4af0bf07c16429",
        "name": "Redmi Note 9 Pro",
        "target_price":17000
    }


]

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find("div", {"class": "_30jeq3 _16Jk6d"})
    if (product_price == None):
        product_price = soup.find(id="priceblock_ourprice")



    return product_price.getText()

result_file = open('my_result_file.txt','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + " - " + every_product.get("name"))

        my_product_price = product_price_returned[1:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)
        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get(
                "name") + ' -  \t' + ' Available at Target Price ' + ' Current Price - ' + str(my_product_price) + '\n')

        else:
            print("Still at current price")

finally :
    result_file.close()





