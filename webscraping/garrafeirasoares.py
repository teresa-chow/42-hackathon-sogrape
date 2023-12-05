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

def mateus_gs(cont, soup):
	named_tuple = time.localtime()
	time_string = time.strftime("%H:%M:%S %d/%m/%Y", named_tuple)

	all = soup.find_all('article', class_="product")
	for x in all:
		everything = x.find(class_="desc")
		name = everything.find('p', class_="name").text
		if (name == 'Vinho Rosé Mateus 75 Cl'):
			price = everything.find('p', class_="current").text
			if (everything.find('p', class_="old")):
				cont['discount'] = "YES"
			else:
				cont['discount'] = "NO"
			if (price.find("€") > 0):
				cont['currency'] = "€"
			cont['price'] = float(price.strip().replace('€', '').replace(',', '.'))
			cont['capacity'] = "750ml"
			name = name.split(" 75 Cl")
			cont['wine'] = name[0]
			cont['harv_year'] = "N/A"
			html_element = soup.find('html')
			lang_value = html_element.get('lang')
			cont['location'] = lang_value
			cont['scrap_date'] = time_string
			cont['shop_name'] = "Garrafeira Soares"
			cont['ean'] = "5601012011500"
			cont['path'] = "./img/Mateus Rosé Original.jpg"
	pprint(cont)
	cont = clean_list(cont)

def mateus_sparkling_gs(cont, soup):
	named_tuple = time.localtime()
	time_string = time.strftime("%H:%M:%S %d/%m/%Y", named_tuple)

	all = soup.find_all('article', class_="product")
	for x in all:
		everything = x.find(class_="desc")
		name = everything.find('p', class_="name").text
		if (name == 'Espumante Mateus Rosé 75 Cl'):
			price = everything.find('p', class_="current").text
			if (everything.find('p', class_="old")):
				cont['discount'] = "YES"
			else:
				cont['discount'] = "NO"
			if (price.find("€") > 0):
				cont['currency'] = "€"
			cont['price'] = float(price.strip().replace('€', '').replace(',', '.'))
			cont['capacity'] = "750ml"
			name = name.split(" 75 Cl")
			cont['wine'] = name[0]
			cont['harv_year'] = "N/A"
			html_element = soup.find('html')
			lang_value = html_element.get('lang')
			cont['location'] = lang_value
			cont['scrap_date'] = time_string
			cont['shop_name'] = "Garrafeira Soares"
			cont['ean'] = "5601012001310"
			cont['path'] = "./img/Mateus Sparkling Rosé.jpg"
	pprint(cont)
	cont = clean_list(cont)

def trb_gs(cont, soup):
	named_tuple = time.localtime()
	time_string = time.strftime("%H:%M:%S %d/%m/%Y", named_tuple)

	all = soup.find_all('article', class_="product")
	for x in all:
		everything = x.find(class_="desc")
		name = everything.find('p', class_="name").text
		if (name == 'Vinho Tinto Trinca Bolotas 75 Cl'):
			price = everything.find('p', class_="current").text
			if (everything.find('p', class_="old")):
				cont['discount'] = "YES"
			else:
				cont['discount'] = "NO"
			if (price.find("€") > 0):
				cont['currency'] = "€"
			cont['price'] = float(price.strip().replace('€', '').replace(',', '.'))
			cont['capacity'] = "750ml"
			name = name.split(" 75 Cl")
			cont['wine'] = name[0]
			cont['harv_year'] = "N/A"
			html_element = soup.find('html')
			lang_value = html_element.get('lang')
			cont['location'] = lang_value
			cont['scrap_date'] = time_string
			cont['shop_name'] = "Garrafeira Soares"
			cont['ean'] = "5601012004427"
			cont['path'] = "./img/Herdade do Peso Trinca Bolotas Tinto.jpg"
	pprint(cont)
	cont = clean_list(cont)

def ppf_gs(cont, soup):
	named_tuple = time.localtime()
	time_string = time.strftime("%H:%M:%S %d/%m/%Y", named_tuple)

	all = soup.find_all('article', class_="product")
	for x in all:
		everything = x.find(class_="desc")
		name = everything.find('p', class_="name").text
		if (name == 'Vinho Branco Douro Papa Figos 75 Cl'):
			price = everything.find('p', class_="current").text
			if (everything.find('p', class_="old")):
				cont['discount'] = "YES"
			else:
				cont['discount'] = "NO"
			if (price.find("€") > 0):
				cont['currency'] = "€"
			cont['price'] = float(price.strip().replace('€', '').replace(',', '.'))
			cont['capacity'] = "750ml"
			name = name.split(" 75 Cl")
			cont['wine'] = name[0]
			cont['harv_year'] = "N/A"
			html_element = soup.find('html')
			lang_value = html_element.get('lang')
			cont['location'] = lang_value
			cont['scrap_date'] = time_string
			cont['shop_name'] = "Garrafeira Soares"
			cont['ean'] = "5601012011920"
			cont['path'] = "./img/Casa Ferreirinha Papa Figos Branco.jpg"
	pprint(cont)
	cont = clean_list(cont)
