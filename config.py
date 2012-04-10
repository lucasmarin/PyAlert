from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import json

buscape_applictation_id = "552f4341373042533847673d"
google_application_id = "AIzaSyCd_rxKDpeDXUx1uFYXzdaUzmbawAuvbxo"

query = "40PFL6606"
price = "1900"

offers_buscape = []
offers_google = []

def buscape():

    url = "http://sandbox.buscape.com/service/findProductList/" + buscape_applictation_id + "/?keyword=" + query + "&format=json"
    req = Request(url)

    try:
        r1 = urlopen(req)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        prod_dict = json.loads( r1.read().decode("utf8") )
        links = prod_dict["product"][0]["product"]["links"]
        for v in links:
            link = v["link"]
            if link["type"] == "xml":
                product_link = link["url"]

    try:
        r2 = urlopen(product_link)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        offer_dict = json.loads( r2.read().decode("utf8") )["offer"]
        for offer in offer_dict:
            of = offer["offer"]
            prod_price = of["price"]["value"]
            if prod_price <= price:
                offers_buscape.append( { of["outlink"] : prod_price } )

buscape()
