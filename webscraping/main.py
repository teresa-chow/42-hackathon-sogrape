import requests
import sys
from bs4 import BeautifulSoup
from pprint import pprint
from continente import mateus_cont, mateus_spark_cont, trinca_bol_cont, papa_fig_cont
from elcorteingles import mateus_elc, mateus_spark_elc, trb_elc, ppf_elc
from garrafeirasoares import mateus_gs, mateus_sparkling_gs, trb_gs, ppf_gs
from elcorteingles_es import mateus_elc_es, trb_elc_es
from pysql import insert_wine, get_search_list

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

def	mateus_origin(headers, cont, flag):
	if (flag == 1):
		link = request_url('https://www.continente.pt/pesquisa/?q=mateus&start=0&srule=Continente&pmin=0.01', headers)
		soup = soup_init(link)
		mateus_cont(cont, soup)
	elif (flag == 2):
		link = request_url('https://www.elcorteingles.pt/supermercado/pesquisar/?term=mateus&search=text', headers)
		soup = soup_init(link)
		mateus_elc(cont, soup)
	elif (flag == 3):
		link = request_url('https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=mateus', headers)
		soup = soup_init(link)
		mateus_gs(cont, soup)
	elif (flag == 4):
		link = request_url('https://www.elcorteingles.es/supermercado/bebidas/vinos/vinos-internacionales/vinos-de-portugal/buscar/?term=mateus', headers)
		soup = soup_init(link)
		mateus_elc_es(cont, soup)
	elif (flag == 0):
		link = request_url('https://www.continente.pt/pesquisa/?q=mateus&start=0&srule=Continente&pmin=0.01', headers)
		soup = soup_init(link)
		mateus_cont(cont, soup)
		link = request_url('https://www.elcorteingles.pt/supermercado/pesquisar/?term=mateus&search=text', headers)
		soup = soup_init(link)
		mateus_elc(cont, soup)
		link = request_url('https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=mateus', headers)
		soup = soup_init(link)
		mateus_gs(cont, soup)
		link = request_url('https://www.elcorteingles.es/supermercado/bebidas/vinos/vinos-internacionales/vinos-de-portugal/buscar/?term=mateus', headers)
		soup = soup_init(link)
		mateus_elc_es(cont, soup)

def	mateus_spark(headers, cont, flag):
	if (flag == 1):
		link = request_url('https://www.continente.pt/pesquisa/?q=mateus&start=0&srule=Continente&pmin=0.01', headers)
		soup = soup_init(link)
		mateus_spark_cont(cont, soup)
	elif (flag == 2):
		link = request_url('https://www.elcorteingles.pt/supermercado/pesquisar/?term=mateus&search=text', headers)
		soup = soup_init(link)
		mateus_spark_elc(cont, soup)
	elif (flag == 3):
		link = request_url('https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=mateus', headers)
		soup = soup_init(link)
		mateus_sparkling_gs(cont, soup)
	elif (flag == 0):
		link = request_url('https://www.continente.pt/pesquisa/?q=mateus&start=0&srule=Continente&pmin=0.01', headers)
		soup = soup_init(link)
		mateus_spark_cont(cont, soup)
		link = request_url('https://www.elcorteingles.pt/supermercado/pesquisar/?term=mateus&search=text', headers)
		soup = soup_init(link)
		mateus_spark_elc(cont, soup)
		link = request_url('https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=mateus', headers)
		soup = soup_init(link)
		mateus_sparkling_gs(cont, soup)

def	trinca_bols(headers, cont, flag):
	if (flag == 1):
		link = request_url('https://www.continente.pt/pesquisa/?q=trinca+bolotas&start=0&srule=Continente&pmin=0.01', headers)
		soup = soup_init(link)
		trinca_bol_cont(cont, soup)
	elif (flag == 2):
		link = request_url('https://www.elcorteingles.pt/supermercado/pesquisar/?term=trinca+bolotas&search=text', headers)
		soup = soup_init(link)
		trb_elc(cont, soup)
	elif (flag == 3):
		link = request_url('https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=trinca+bolotas', headers)
		soup = soup_init(link)
		trb_gs(cont, soup)
	elif (flag == 4):
		link = request_url('https://www.elcorteingles.es/supermercado/bebidas/vinos/vinos-internacionales/vinos-de-portugal/buscar/?term=trinca%20bolotas', headers)
		soup = soup_init(link)
		trb_elc_es(cont, soup)
	elif (flag == 0):
		link = request_url('https://www.continente.pt/pesquisa/?q=trinca+bolotas&start=0&srule=Continente&pmin=0.01', headers)
		soup = soup_init(link)
		trinca_bol_cont(cont, soup)
		link = request_url('https://www.elcorteingles.pt/supermercado/pesquisar/?term=trinca+bolotas&search=text', headers)
		soup = soup_init(link)
		trb_elc(cont, soup)
		link = request_url('https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=trinca+bolotas', headers)
		soup = soup_init(link)
		trb_gs(cont, soup)
		link = request_url('https://www.elcorteingles.es/supermercado/bebidas/vinos/vinos-internacionales/vinos-de-portugal/buscar/?term=trinca%20bolotas', headers)
		soup = soup_init(link)
		trb_elc_es(cont, soup)

def	papa_figos(headers, cont, flag):
	if (flag == 1):
		link = request_url('https://www.continente.pt/pesquisa/?q=papa+figos&start=0&srule=Continente%2004&pmin=0.01', headers)
		soup = soup_init(link)
		papa_fig_cont(cont, soup)
	elif (flag == 2):
		link = request_url('https://www.elcorteingles.pt/supermercado/pesquisar/?term=papa+figos&search=text', headers)
		soup = soup_init(link)
		ppf_elc(cont, soup)
	elif (flag == 3):
		link = request_url('https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=papa+figos', headers)
		soup = soup_init(link)
		ppf_gs(cont, soup)
	elif (flag == 0):
		link = request_url('https://www.continente.pt/pesquisa/?q=papa+figos&start=0&srule=Continente%2004&pmin=0.01', headers)
		soup = soup_init(link)
		papa_fig_cont(cont, soup)
		link = request_url('https://www.elcorteingles.pt/supermercado/pesquisar/?term=papa+figos&search=text', headers)
		soup = soup_init(link)
		ppf_elc(cont, soup)
		link = request_url('https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=papa+figos', headers)
		soup = soup_init(link)
		ppf_gs(cont, soup)
  ######################################################3
 
def searchwine(headers, cont, flag, ean, name, year, cap):
	if (flag == 1):
		link = request_url(f'https://www.continente.pt/pesquisa/?q={ean}&start=0&srule=Continente&pmin=0.01', headers)
		soup = soup_init(link)
		cont_search(cont, soup, ean, name, year, cap)
	elif (flag == 2):
		link = request_url(f'https://www.elcorteingles.pt/supermercado/pesquisar/?term={ean}&search=text', headers)
		soup = soup_init(link)
		elcpt_search(cont, soup, ean, name, year, cap)
	elif (flag == 3):
		link = request_url(f'https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term={ean}', headers)
		soup = soup_init(link)
		mateus_gs(cont, soup)
	elif (flag == 4):
		link = request_url(f'https://www.elcorteingles.es/supermercado/bebidas/vinos/vinos-internacionales/vinos-de-portugal/buscar/?term={ean}', headers)
		soup = soup_init(link)
		mateus_elc_es(cont, soup)
	# elif (flag == 0):
	# 	link = request_url(f'https://www.continente.pt/pesquisa/?q={ean}&start=0&srule=Continente&pmin=0.01', headers)
	# 	soup = soup_init(link)
	# 	shop = "continente"
	# 	mateus_cont(cont, soup, shop)
	# 	link = request_url(f'https://www.elcorteingles.pt/supermercado/pesquisar/?term={ean}&search=text', headers)
	# 	soup = soup_init(link)
	# 	mateus_elc(cont, soup)
	# 	link = request_url(f'https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term={ean}', headers)
	# 	soup = soup_init(link)
	# 	mateus_gs(cont, soup)
	# 	link = request_url(f'https://www.elcorteingles.es/supermercado/bebidas/vinos/vinos-internacionales/vinos-de-portugal/buscar/?term={ean}', headers)
	# 	soup = soup_init(link)
	# 	mateus_elc_es(cont, soup)

################# SEARCHES FIX - Any Wine ###############

def cont_search(cont, soup, ean, name, year, cap):
	all = soup.find_all(class_="ct-inner-tile-wrap col-inner-tile-wrap row no-gutters justify-content-center align-content-start")
	for x in all:
		everything = x.find("a", class_="pwc-tile--description col-tile--description")
		print(name)
		print(everything.text)
		if (name in everything.text):
			#if (x.find("p", class_="pwc-tile--quantity col-tile--quantity").text == "garrafa 37,5 cl"):
				price = x.find(class_="pwc-price-wrap col-8 col-sm-12")
				final_price = price.find(class_="ct-price-formatted")
				if (final_price.text.find("€") == 1):
					cont['currency'] = "€"
				cont['capacity'] = cap
				cont['wine'] = everything.text
				cont['price'] = float(final_price.text.strip().replace('€', '').replace(',', '.'))
				cont['harv_year'] = "N/A"
				html_element = soup.find('html')
				lang_value = html_element.get('lang')
				cont['location'] = lang_value
				if (x.find(class_="pwc-discount-amount col-discount-amount") != None):
					cont['discount'] = "YES"
				else:
					cont['discount'] = "NO"
				cont['shop_name'] = "Continente"
				cont['ean'] = ean
				cont['path'] = "./img/Mateus Rosé Original.jpg"
	pprint(cont)
	insert_wine(cont)
	cont = clean_list(cont)

def elcpt_search(cont, soup, ean, name, year, cap):
	all = soup.find_all(class_="grid-item product_tile _retro _supermarket dataholder js-product")
	for x in all:
		everything = x.find(class_="product_tile-right_container")
		only_desc = everything.find('a', class_="link event js-product-link")
		if (name in only_desc.text):
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
			cont['capacity'] = cap
			wine_name = only_desc.text.strip()
			wine_name = wine_name.split(" garrafa")
			cont['wine'] = wine_name[0]
			pprint(wine_name)
			cont['harv_year'] = "N/A"
			html_element = soup.find('html')
			lang_value = html_element.get('lang')
			cont['location'] = lang_value
			cont['shop_name'] = "El Corte Inglés"
			cont['ean'] = ean
			cont['path'] = "./img/Mateus Rosé Original.jpg"
	pprint(cont)
	insert_wine(cont)
	cont = clean_list(cont)
 
def garrf_search(cont, soup, ean, name2, year, cap):
	all = soup.find_all('article', class_="product")
	for x in all:
		everything = x.find(class_="desc")
		name = everything.find('p', class_="name").text
		if (name2 in name):
			price = everything.find('p', class_="current").text
			if (everything.find('p', class_="old")):
				cont['discount'] = "YES"
			else:
				cont['discount'] = "NO"
			if (price.find("€") > 0):
				cont['currency'] = "€"
			cont['price'] = float(price.strip().replace('€', '').replace(',', '.'))
			cont['capacity'] = cap
			name = name.split(" 75 Cl")
			cont['wine'] = name[0]
			cont['harv_year'] = "N/A"
			html_element = soup.find('html')
			lang_value = html_element.get('lang')
			cont['location'] = lang_value
			cont['shop_name'] = "Garrafeira Soares"
			cont['ean'] = ean
			cont['path'] = "./img/Mateus Rosé Original.jpg"
	pprint(cont)
	insert_wine(cont)
	cont = clean_list(cont)
 
def ecles_search(cont, soup, ean, name, year, cap):

	all = soup.find_all(class_="grid-item product_tile _retro _supermarket dataholder js-product")
	for x in all:
		everything = x.find(class_="product_tile-right_container")
		only_desc = everything.find('a', class_="link event js-product-link")
		if (name in only_desc.text):
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
			wine_name = wine_name.split(" botella")
			cont['wine'] = wine_name[0]
			cont['harv_year'] = "N/A"
			html_element = soup.find('html')
			lang_value = html_element.get('lang')
			cont['location'] = lang_value
			cont['shop_name'] = "El Corte Inglés_Es"
			cont['ean'] = ean
			cont['path'] = "./img/Mateus Rosé Original.jpg"
	pprint(cont)
	insert_wine(cont)
	cont = clean_list(cont)

############################################################################
def	continente(headers, ean, name, year, cap):
	cont = {
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
	flag = 1
	# mateus_origin(headers, cont, flag)
	# insert_wine(cont)
	# mateus_spark(headers, cont, flag)
	# insert_wine(cont)
	# trinca_bols(headers, cont, flag)
	# insert_wine(cont)
	# papa_figos(headers, cont, flag)
	searchwine(headers, cont, flag, ean, name, year, cap)
 
def	elcorteingles(headers, ean, name, year, cap):
	cont = {
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
	flag = 2
	# mateus_origin(headers, cont, flag)
	# insert_wine(cont)
	# mateus_spark(headers, cont, flag)
	# insert_wine(cont)
	# trinca_bols(headers, cont, flag)
	# insert_wine(cont)
	# papa_figos(headers, cont, flag)
	# insert_wine(cont)
	searchwine(headers, cont, flag, ean, name, year, cap)

def	garrafeirasoares(headers, ean, name, year, cap):
	cont = {
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
	flag = 3
	# mateus_origin(headers, cont, flag)
	# insert_wine(cont)
	# mateus_spark(headers, cont, flag)
	# insert_wine(cont)
	# trinca_bols(headers, cont, flag)
	# insert_wine(cont)
	# papa_figos(headers, cont, flag)
	# insert_wine(cont)
	searchwine(headers, cont, flag, ean, name, year, cap)

def	elcorteingles_es(headers, ean, name, year, cap):
	cont = {
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
	flag = 4
	# mateus_origin(headers, cont, flag)
	# insert_wine(cont)
	# trinca_bols(headers, cont, flag)
	# insert_wine(cont)
	searchwine(headers, cont, flag, ean, name, year, cap)
 
 #################################################
 
def	continente2(headers):
	cont = {
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
	flag = 1
	mateus_origin(headers, cont, flag)
	insert_wine(cont)
	mateus_spark(headers, cont, flag)
	insert_wine(cont)
	trinca_bols(headers, cont, flag)
	insert_wine(cont)
	papa_figos(headers, cont, flag)
 
def	elcorteingles2(headers):
	cont = {
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
	flag = 2
	mateus_origin(headers, cont, flag)
	insert_wine(cont)
	mateus_spark(headers, cont, flag)
	insert_wine(cont)
	trinca_bols(headers, cont, flag)
	insert_wine(cont)
	papa_figos(headers, cont, flag)
	insert_wine(cont)

def	garrafeirasoares2(headers):
	cont = {
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
	flag = 3
	mateus_origin(headers, cont, flag)
	insert_wine(cont)
	mateus_spark(headers, cont, flag)
	insert_wine(cont)
	trinca_bols(headers, cont, flag)
	insert_wine(cont)
	papa_figos(headers, cont, flag)
	insert_wine(cont)

def	elcorteingles_es2(headers):
	cont = {
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
	flag = 4
	mateus_origin(headers, cont, flag)
	insert_wine(cont)
	trinca_bols(headers, cont, flag)
	insert_wine(cont)
 
 #################################################

def	soup_init(link):
	soup = BeautifulSoup(link.content, 'html.parser')
	return soup

def	request_url(url, headers):
	link = requests.get(url, headers=headers)
	return link

def initvalues():
	headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
	}
	return headers

def main():
	headers = initvalues()
	# name = input("Shops available:\n(0) SCRAPE ALL\n(1) Continente\n(2) El Corte Ingles\n(3) Garrafeira Soares\n(4) El Corte Ingles_Es\nChoose a number: ")
	# # if (name == "0"):
	# # 	flag = 0
	# # 	continente(headers, flag)
	# # 	elcorteingles(headers, flag)
	# # 	garrafeirasoares(headers, flag)
	# # 	elcorteingles_es(headers, flag)
	# if (name == "1"):
	# 	continente(headers)
	# elif (name == "2"):
	# 	elcorteingles(headers)
	# elif (name == "3"):
	# 	garrafeirasoares(headers)
	# elif (name == "4"):
	# 	elcorteingles_es(headers)
	# else:
	continente2(headers)
	elcorteingles2(headers)
	garrafeirasoares2(headers)
	elcorteingles_es2(headers)
	data = get_search_list()
	for item in data:
		ean = item[1]
		name = item[2]
		year = item[3]
		cap = item[4]
		print(f"\n\n\nNow inserting new wine manually given: {name}\n\n\n")
		continente(headers, ean, name, year, cap)
		elcorteingles(headers, ean, name, year, cap)
		garrafeirasoares(headers, ean, name, year, cap)
		elcorteingles_es(headers, ean, name, year, cap)

# EAN Mateus OG     : 5601012011500		path:"./img/Mateus Rosé Original.jpg"
# EAN Mateus Spark  : 5601012001310		path:"./img/Mateus Sparkling Rosé.jpg"
# EAN Trinca Bolotas: 5601012004427		path:"./img/Herdade do Peso Trinca Bolotas Tinto.jpg"
# EAN Papa Figos    : 5601012011920		path:"./img/Casa Ferreirinha Papa Figos Branco.jpg"

if __name__ == "__main__":
    main()
