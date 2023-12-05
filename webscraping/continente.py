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

def mateus_cont(cont, soup):
	named_tuple = time.localtime()
	time_string = time.strftime("%H:%M:%S %d/%m/%Y", named_tuple)

	all = soup.find_all(class_="ct-inner-tile-wrap col-inner-tile-wrap row no-gutters justify-content-center align-content-start")
	for x in all:
		everything = x.find("a", class_="pwc-tile--description col-tile--description")
		if (everything.text == 'Mateus Vinho Rosé'):
			if (x.find("p", class_="pwc-tile--quantity col-tile--quantity").text == "garrafa 37,5 cl"):
				price = x.find(class_="pwc-price-wrap col-8 col-sm-12")
				final_price = price.find(class_="ct-price-formatted")
				if (final_price.text.find("€") == 1):
					cont['currency'] = "€"
				cont['capacity'] = "750ml"
				cont['wine'] = everything.text
				cont['price'] = float(final_price.text.strip().replace('€', '').replace(',', '.'))
				cont['harv_year'] = "N/A"
				html_element = soup.find('html')
				lang_value = html_element.get('lang')
				cont['location'] = lang_value
				cont['scrap_date'] = time_string
				if (x.find(class_="pwc-discount-amount col-discount-amount") != None):
					cont['discount'] = "YES"
				else:
					cont['discount'] = "NO"
				cont['shop_name'] = "Continente"
				cont['ean'] = "5601012011500"
				cont['path'] = "./img/Mateus Rosé Original.jpg"
	pprint(cont)
	cont = clean_list(cont)

def	mateus_spark_cont(cont, soup):
	named_tuple = time.localtime()
	time_string = time.strftime("%H:%M:%S %d/%m/%Y", named_tuple)

	all = soup.find_all(class_="ct-inner-tile-wrap col-inner-tile-wrap row no-gutters justify-content-center align-content-start")
	for x in all:
		everything = x.find("a", class_="pwc-tile--description col-tile--description")
		if (everything.text == 'Mateus Sparkling Espumante Rosé Bruto'):
			if (x.find("p", class_="pwc-tile--quantity col-tile--quantity").text == "garrafa 75 cl"):
				price = x.find(class_="pwc-price-wrap col-8 col-sm-12")
				final_price = price.find(class_="ct-price-formatted")
				if (final_price.text.find("€") == 1):
					cont['currency'] = "€"
				cont['capacity'] = "750ml"
				cont['wine'] = everything.text
				cont['price'] = float(final_price.text.strip().replace('€', '').replace(',', '.'))
				cont['harv_year'] = "N/A"
				html_element = soup.find('html')
				lang_value = html_element.get('lang')
				cont['location'] = lang_value
				cont['scrap_date'] = time_string
				if (x.find(class_="pwc-discount-amount col-discount-amount") != None):
					cont['discount'] = "YES"
				else:
					cont['discount'] = "NO"
				cont['shop_name'] = "Continente"
				cont['ean'] = "5601012001310"
				cont['path'] = "./img/Mateus Sparkling Rosé.jpg"
	pprint(cont)
	cont = clean_list(cont)

def	trinca_bol_cont(cont, soup):
	named_tuple = time.localtime()
	time_string = time.strftime("%H:%M:%S %d/%m/%Y", named_tuple)

	all = soup.find_all(class_="ct-inner-tile-wrap col-inner-tile-wrap row no-gutters justify-content-center align-content-start")
	for x in all:
		everything = x.find("a", class_="pwc-tile--description col-tile--description")
		if (everything.text == 'Trinca Bolotas Regional Alentejano Vinho Tinto'):
			if (x.find("p", class_="pwc-tile--quantity col-tile--quantity").text == "garrafa 75 cl"):
				price = x.find(class_="pwc-price-wrap col-8 col-sm-12")
				final_price = price.find(class_="ct-price-formatted")
				if (final_price.text.find("€") == 1):
					cont['currency'] = "€"
				cont['capacity'] = "750ml"
				cont['wine'] = everything.text
				cont['price'] = float(final_price.text.strip().replace('€', '').replace(',', '.'))
				cont['harv_year'] = "N/A"
				html_element = soup.find('html')
				lang_value = html_element.get('lang')
				cont['location'] = lang_value
				cont['scrap_date'] = time_string
				if (x.find(class_="pwc-discount-amount col-discount-amount") != None):
					cont['discount'] = "YES"
				else:
					cont['discount'] = "NO"
				cont['shop_name'] = "Continente"
				cont['ean'] = "5601012004427"
				cont['path'] = "./img/Herdade do Peso Trinca Bolotas Tinto.jpg"
	pprint(cont)
	cont = clean_list(cont)

def	papa_fig_cont(cont, soup):
	named_tuple = time.localtime()
	time_string = time.strftime("%H:%M:%S %d/%m/%Y", named_tuple)

	all = soup.find_all(class_="ct-inner-tile-wrap col-inner-tile-wrap row no-gutters justify-content-center align-content-start")
	for x in all:
		everything = x.find("a", class_="pwc-tile--description col-tile--description")
		if (everything.text == 'Papa Figos DOC Douro Vinho Branco'):
			if (x.find("p", class_="pwc-tile--quantity col-tile--quantity").text == "garrafa 75 cl"):
				price = x.find(class_="pwc-price-wrap col-8 col-sm-12")
				final_price = price.find(class_="ct-price-formatted")
				if (final_price.text.find("€") == 1):
					cont['currency'] = "€"
				cont['capacity'] = "750ml"
				cont['wine'] = everything.text
				cont['price'] = float(final_price.text.strip().replace('€', '').replace(',', '.'))
				cont['harv_year'] = "N/A"
				html_element = soup.find('html')
				lang_value = html_element.get('lang')
				cont['location'] = lang_value
				cont['scrap_date'] = time_string
				if (x.find(class_="pwc-discount-amount col-discount-amount") != None):
					cont['discount'] = "YES"
				else:
					cont['discount'] = "NO"
				cont['shop_name'] = "Continente"
				cont['ean'] = "5601012011920"
				cont['path'] = "./img/Casa Ferreirinha Papa Figos Branco.jpg"
	pprint(cont)
	cont = clean_list(cont)
