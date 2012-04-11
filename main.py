from setup import *
from pyalert.shops.buscape import Buscape

buscape = Buscape( BUSCAPE_APPLICATION_ID, PRICE )
buscape_result = buscape.findProductList( QUERY )
print(buscape_result)

