from ..setup import setup
from .shops import buscape

buscape = Buscape( buscape_application_id, price )
buscape_result = buscape.findProductList( query )
print(buscape_result)
