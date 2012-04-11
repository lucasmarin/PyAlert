from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from json import loads

class Buscape():

    format = "json"
    url = "http://sandbox.buscape.com/service/%s/%s/?keyword=%s&format=%s"

    def __init__( application_id, price = None ):
        if ( !price ):
            price = global price
        self.price = price;
        self.application_id = application_id
    
    def request( url ):
        try:
            req = Request(url)
            response = urlopen(req)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
        except URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        else:
            return response.read().decode("utf8")
    
    def findProductList(query):

        offers_buscape = []
        
        url = self.url % ( "findProductList", self.application_id, query, self.format )
        response = request(url)
        prod_dict = json.loads( response )
        links = prod_dict["product"][0]["product"]["links"]
        for v in links:
            link = v["link"]
            if link["type"] == "xml":
                product_link = link["url"]

        response = request(product_link)
        offer_dict = json.loads( response )["offer"]
        for offer in offer_dict:
            of = offer["offer"]
            prod_price = of["price"]["value"]
            if prod_price <= self.price:
                offers_buscape.append( { of["outlink"] : prod_price } )

        return offers_buscape
