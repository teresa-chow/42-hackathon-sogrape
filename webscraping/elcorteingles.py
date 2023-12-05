import time
from pprint import pprint

def	clean_list(list):
	list = {
		'shop_name': '',
		'ean': '',
		'path': '',
		'wine': '',
		'harv_year': '',
		'capacity': '',
		'price': '',
		'discount': '',
		'currency': '',
		'scrap_date': '',
		'location': ''
	}
	return list

def mateus_elc(cont, soup):
	named_tuple = time.localtime()
	time_string = time.strftime("%H:%M:%S %d/%m/%Y", named_tuple)

	all = soup.find_all(class_="grid-item product_tile _retro _supermarket dataholder js-product")
	for x in all:
		everything = x.find(class_="product_tile-right_container")
		only_desc = everything.find('a', class_="link event js-product-link")
		if (only_desc.text == 'Mateus Vinho Rosé garrafa 75 cl '):
			if (everything.find(class_="prices-price _current")):
				price = everything.find(class_="prices-price _current").text
				if (price.find("€") > 0):
					cont['currency'] = "€"
				cont['price'] = float(price.replace(',', '.').replace('€', ''))
				cont['discount'] = "NO"
			elif (everything.find(class_="prices-price _offer")):
				price = everything.find(class_="prices-price _offer").text
				if (price.find("€") > 0):
					cont['currency'] = "€"
				cont['price'] = float(price.replace(',', '.').replace('€', ''))
				cont['discount'] = "YES"
			cont['capacity'] = "750ml"
			wine_name = only_desc.text.strip()
			wine_name = wine_name.split(" garrafa")
			cont['wine'] = wine_name[0]
			pprint(wine_name)
			cont['harv_year'] = "N/A"
			html_element = soup.find('html')
			lang_value = html_element.get('lang')
			cont['location'] = lang_value
			cont['scrap_date'] = time_string
			cont['shop_name'] = "El Corte Inglés"
			cont['ean'] = "5601012011500"
			cont['path'] = "./img/Mateus Rosé Original.jpg"
	pprint(cont)
	cont = clean_list(cont)

def mateus_spark_elc(cont, soup):
	named_tuple = time.localtime()
	time_string = time.strftime("%H:%M:%S %d/%m/%Y", named_tuple)

	all = soup.find_all(class_="grid-item product_tile _retro _supermarket dataholder js-product")
	for x in all:
		everything = x.find(class_="product_tile-right_container")
		only_desc = everything.find('a', class_="link event js-product-link")
		if (only_desc.text == 'Mateus Espumante Sparkling Rosé Bruto garrafa 75 cl '):
			if (everything.find(class_="prices-price _current")):
				price = everything.find(class_="prices-price _current").text
				if (price.find("€") > 0):
					cont['currency'] = "€"
				cont['price'] = float(price.replace(',', '.').replace('€', ''))
				cont['discount'] = "NO"
			elif (everything.find(class_="prices-price _offer")):
				price = everything.find(class_="prices-price _offer").text
				if (price.find("€") > 0):
					cont['currency'] = "€"
				cont['price'] = float(price.replace(',', '.').replace('€', ''))
				cont['discount'] = "YES"
			cont['capacity'] = "750ml"
			wine_name = only_desc.text.strip()
			wine_name = wine_name.split(" garrafa")
			cont['wine'] = wine_name[0]
			cont['harv_year'] = "N/A"
			html_element = soup.find('html')
			lang_value = html_element.get('lang')
			cont['location'] = lang_value
			cont['scrap_date'] = time_string
			cont['shop_name'] = "El Corte Inglés"
			cont['ean'] = "5601012001310"
			cont['path'] = "./img/Mateus Sparkling Rosé.jpg"
	pprint(cont)
	cont = clean_list(cont)

def trb_elc(cont, soup):
	named_tuple = time.localtime()
	time_string = time.strftime("%H:%M:%S %d/%m/%Y", named_tuple)

	all = soup.find_all(class_="grid-item product_tile _retro _supermarket dataholder js-product")
	for x in all:
		everything = x.find(class_="product_tile-right_container")
		only_desc = everything.find('a', class_="link event js-product-link")
		if (only_desc.text == 'Trinca Bolotas Vinho Tinto Regional do Alentejo garrafa 75 cl '):
			if (everything.find(class_="prices-price _current")):
				price = everything.find(class_="prices-price _current").text
				if (price.find("€") > 0):
					cont['currency'] = "€"
				cont['price'] = float(price.replace(',', '.').replace('€', ''))
				cont['discount'] = "NO"
			elif (everything.find(class_="prices-price _offer")):
				price = everything.find(class_="prices-price _offer").text
				if (price.find("€") > 0):
					cont['currency'] = "€"
				cont['price'] = float(price.replace(',', '.').replace('€', ''))
				cont['discount'] = "YES"
			cont['capacity'] = "750ml"
			wine_name = only_desc.text.strip()
			wine_name = wine_name.split(" garrafa")
			cont['wine'] = wine_name[0]
			cont['harv_year'] = "N/A"
			html_element = soup.find('html')
			lang_value = html_element.get('lang')
			cont['location'] = lang_value
			cont['scrap_date'] = time_string
			cont['shop_name'] = "El Corte Inglés"
			cont['ean'] = "5601012004427"
			cont['path'] = "./img/Herdade do Peso Trinca Bolotas Tinto.jpg"
	pprint(cont)
	cont = clean_list(cont)

def ppf_elc(cont, soup):
	named_tuple = time.localtime()
	time_string = time.strftime("%H:%M:%S %d/%m/%Y", named_tuple)

	all = soup.find_all(class_="grid-item product_tile _retro _supermarket dataholder js-product")
	for x in all:
		everything = x.find(class_="product_tile-right_container")
		only_desc = everything.find('a', class_="link event js-product-link")
		if (only_desc.text == 'Papa Figos Vinho Branco do Douro garrafa 75 cl '):
			if (everything.find(class_="prices-price _current")):
				price = everything.find(class_="prices-price _current").text
				if (price.find("€") > 0):
					cont['currency'] = "€"
				cont['price'] = float(price.replace(',', '.').replace('€', ''))
				cont['discount'] = "NO"
			elif (everything.find(class_="prices-price _offer")):
				price = everything.find(class_="prices-price _offer").text
				if (price.find("€") > 0):
					cont['currency'] = "€"
				cont['price'] = float(price.replace(',', '.').replace('€', ''))
				cont['discount'] = "YES"
			cont['capacity'] = "750ml"
			wine_name = only_desc.text.strip()
			wine_name = wine_name.split(" garrafa")
			cont['wine'] = wine_name[0]
			cont['harv_year'] = "N/A"
			html_element = soup.find('html')
			lang_value = html_element.get('lang')
			cont['location'] = lang_value
			cont['scrap_date'] = time_string
			cont['shop_name'] = "El Corte Inglés"
			cont['ean'] = "5601012011920"
			cont['path'] = "./img/Casa Ferreirinha Papa Figos Branco.jpg"
	pprint(cont)
	cont = clean_list(cont)
