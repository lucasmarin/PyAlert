from setup import *
from pyalert.shops.buscape import Buscape
import time
import sys
import getopt

def usage(opt=0):
    print("""Usage: main.py [OPTIONS]
Find products in online shops with price and query completeds in parameters and send to mail.

  -h, --help        Print this help
  --price=PRICE     Filters price less than or equal price completed
  --query=QUERY     Query filter to find product
  --to=EMAIL        E-mail to send the found products
  --time=MINUTES    Time interval in minutes to search products. 30(default), 15(min)

Example:
  python """ + str(sys.argv[0]) + """ --price=1800 --query=40PFL6606 --to="test@domain.com, me@me.com" --time=120""")
    sys.exit(opt)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "price=", "query=", "time=", "to="])
    except getopt.GetoptError as msg:
        print(msg)
        print("for help use python " + str(sys.argv[0]) + " --help")
        sys.exit(2)
    else:
        price = None
        query = None
        t = 30
        to = None
        for key, value in opts:
            if key in ("-h", "--help"):
                usage(2)
            if key == "--price":
                price = value
            elif key == "--query":
                query = value
            elif key == "--time":
                t = value
            elif key == "--to":
                to = value
        if price is None or query is None or to is None:
            usage()
        elif float(t) < 15:
            usage()
        else:
            print("Search intilialized...")
            print("Time interval: %s minutes" % (str(t)))
            while(1):
                print("Searching")
                #TODO: Utilizar o google shop
                buscape = Buscape( BUSCAPE_APPLICATION_ID, price )
                buscape_result = buscape.findProductList( query )
                #TODO: Verificar se a busca retornou algum produto independente de preco
                if buscape_result == "[]":
                    print("Nothing found")
                else:
                    #TODO: SEND EMAIL
                    print(buscape_result)
                time.sleep(float(t))                
                
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

